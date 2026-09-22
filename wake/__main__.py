# =============================================================================
# CLI — the human/operator boundary. Commands turn explicit operator intent into engine/store/report operations. Human-only powers such as focus changes, cancellation and destructive reset stay visibly different from model proposals.
#
# MAINTENANCE PRINCIPLE
# ---------------------
# The architecture is intentionally explicit.  A future human or AI maintainer
# should be able to follow authority from input, through validation, to durable
# record without relying on folklore.  Comments explain why boundaries exist,
# what failure means, and which tempting shortcuts would weaken accountability.
# =============================================================================

"""Command line interface. All mutations share the same writer lock."""

import argparse
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
import json
from pathlib import Path
import sqlite3
import sys
import shutil

from .audit import verify_history
from .engine import Engine, config
from .governance import Rejected, require, text
from .providers import Fixture, Gemini, SCHEMA
from .report import atomic_write, export
from .store import IntegrityError
# ---------------------------------------------------------------------------
# STEP: parser
#
# Keep this function explicit because it marks a testable boundary in the
# chain from operator/provider input to durable/public output.  Do not fold it
# into a neighboring layer if doing so would hide validation, provenance,
# failure handling, or the distinction between accepted state and a derived view.
# ---------------------------------------------------------------------------


def parser():
    p = argparse.ArgumentParser(prog="python -m wake", description="Disposable models. Durable state. Receipts for everything.")
    p.add_argument("--data", default="data", help="Durable state directory (default: data)")
    p.add_argument("--config", default="wake.toml")
    sub = p.add_subparsers(dest="command", required=True)
    sub.add_parser("init", help="Initialize an empty record; never overwrite an existing one")
    wake = sub.add_parser("wake", help="Run one bounded invocation")
    wake.add_argument("--provider", choices=["gemini", "fixture"])
    wake.add_argument("--model")
    wake.add_argument("--crash-at", choices=["after-start", "during-commit"], help="Fixture-only crash experiment")
    sub.add_parser("status")
    reset = sub.add_parser("reset", help="Irreversibly return durable state to WAKE 0")
    reset.add_argument("--confirm", action="store_true",
                       help="Confirm deletion of all accumulated WAKE state")
    reset.add_argument("--output", default="site",
                       help="Generated report directory to replace (default: site)")
    recover = sub.add_parser("recover", help="Rebuild a corrupt projection; close an interrupted invocation")
    observe = sub.add_parser("observe", help="Add a human-supplied observation")
    observe.add_argument("--source", required=True)
    observe.add_argument("--text", required=True)
    focus = sub.add_parser("focus", help="Set the next review focus; durable, human-only")
    focus.add_argument("text")
    focus.add_argument("--reason", required=True)
    cancel = sub.add_parser("cancel", help="Cancel an obligation as a human, with a permanent reason")
    cancel.add_argument("id")
    cancel.add_argument("--reason", required=True)
    control = sub.add_parser("time-dilation", help="Record an operator Time Dilation regime change")
    control.add_argument("--enabled", choices=["true", "false"])
    control.add_argument("--mode", choices=["real", "scaled", "frozen"])
    control.add_argument("--scale", type=float)
    control.add_argument("--reason", required=True)
    report = sub.add_parser("export", help="Generate portable HTML, Markdown, state and history")
    report.add_argument("--output", default="site")
    audit = sub.add_parser("audit", help="Verify every event and reconstruct all state")
    audit.add_argument("--events", help="Verify a JSONL export independently of the database")
    audit.add_argument("--head", help="Path to independently retained head.txt, for truncation detection")
    backup = sub.add_parser("backup")
    backup.add_argument("destination")
    prepare = sub.add_parser("prepare", help="Create a durable request for a free desktop model")
    prepare.add_argument("--model", required=True, help="Human-attested provider/model name")
    prepare.add_argument("--output", default="request.json")
    complete = sub.add_parser("complete", help="Validate a manually supplied JSON reply")
    complete.add_argument("--id", required=True)
    complete.add_argument("--file", required=True)
    sub.add_parser("schema", help="Print the proposal JSON schema")
    experiment = sub.add_parser("experiment", help="Run an entirely offline, fresh-process experiment")
    experiment.add_argument("--cycles", type=int, default=100)
    experiment.add_argument("--output", default="site")
    serve = sub.add_parser("serve", help="Serve generated reports only, never the repository or .env")
    serve.add_argument("--directory", default="site")
    serve.add_argument("--host", default="127.0.0.1")
    serve.add_argument("--port", type=int, default=8000)
    return p
# ---------------------------------------------------------------------------
# STEP: execute
#
# Keep this function explicit because it marks a testable boundary in the
# chain from operator/provider input to durable/public output.  Do not fold it
# into a neighboring layer if doing so would hide validation, provenance,
# failure handling, or the distinction between accepted state and a derived view.
# ---------------------------------------------------------------------------


def execute(args):
    if args.command == "schema":
        return SCHEMA
    if args.command == "serve":
        path = Path(args.directory).resolve()
        require((path / "index.html").exists(), "Export a journal before serving it")
        require(not (path / ".env").exists() and not (path / ".git").exists(), "Serve a report directory, not the repository")
        server = ThreadingHTTPServer((args.host, args.port), partial(SimpleHTTPRequestHandler, directory=str(path)))
        print(f"Journal: http://{args.host}:{server.server_port} (Ctrl-C to stop)", flush=True)
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            pass
        finally:
            server.server_close()
        return None
    if args.command == "audit" and args.events:
        state, head = verify_history(args.events, Path(args.head).read_text() if args.head else None)
        return {"valid": True, "cycles": state["version"], "head": head, "source": "exported history only"}
    settings = config(args.config)
    if args.command == "experiment":
        from .experiment import run_experiment
        result = run_experiment(args.data, args.cycles, args.output)
        return {k: v for k, v in result.items() if k != "commands"}
    engine = Engine(args.data, settings)
    try:
        if args.command == "wake":
            name = args.provider or settings["provider"]
            require(not args.crash_at or name == "fixture", "Crash injection is only allowed with fixture providers")
            require(name in ("fixture", "gemini"), "Unsupported provider; use prepare/complete for desktop models")
            provider = Fixture(args.model or "fixture-a") if name == "fixture" else Gemini(settings, args.model)
            from .research import collect
            return engine.run(provider, args.crash_at, collector=collect if name == "gemini" and settings.get("mission") else None)
        if args.command == "export":
            return export(engine.store, args.output)
        if args.command == "reset":
            require(args.confirm, "Reset requires --confirm")
            target = Path(args.output).resolve()
            cwd = Path.cwd().resolve()
            data_dir = engine.store.directory.resolve()
            require(target != cwd and target not in cwd.parents,
                    "Refusing to delete the repository or one of its parent directories")
            require(target != data_dir and target not in data_dir.parents and data_dir not in target.parents,
                    "Refusing to use the durable state directory or one of its parents/children as reset output")
            with engine.store.lock():
                engine.store.reset()
                state = engine.initialize()
            if target.exists():
                shutil.rmtree(target)
            published = export(engine.store, target)
            return {"reset": True, "cycles": state["version"],
                    "head": published["head"], "path": published["path"]}
        with engine.store.lock():
            if args.command == "time-dilation":
                state = engine.initialize()
            if args.command == "init":
                state = engine.initialize()
                return {"initialized": True, "cycles": state["version"]}
            if args.command == "recover":
                state = engine.recover(explicit=True)
                return {"recovered": True, "cycles": state["version"], "pending": state["pending"]}
            state = engine.store.load()
            require(bool(state["objective"]), "Initialize this record first")
            if args.command in ("status", "audit"):
                _, head = engine.store.replay()
                return {"valid": True, "cycles": state["version"], "head": head,
                        "pending": state["pending"], "beliefs": len(state["beliefs"]),
                        "open_commitments": sum(c["status"] == "open" for c in state["commitments"].values()),
                        "invocations": len(state["invocations"])}
            if args.command == "observe":
                result = engine.observe(args.text, args.source)
                return {"evidence": list(result["evidence"])[-1]}
            if args.command in ("focus", "cancel", "time-dilation"):
                require(state["pending"] is None, "Finish or recover the pending invocation first")
                text(args.reason, "Reason")
                if args.command == "focus":
                    text(args.text, "Focus", 1000)
                    engine.store.append("focus_changed", {"focus": args.text, "reason": args.reason, "actor": "human"})
                elif args.command == "cancel":
                    engine.store.append("commitment_cancelled", {"id": args.id, "reason": args.reason, "actor": "human"})
                else:
                    require(any(value is not None for value in (args.enabled, args.mode, args.scale)),
                            "Specify at least one Time Dilation control")
                    engine.set_time_dilation(
                        enabled=None if args.enabled is None else args.enabled == "true",
                        mode=args.mode, scale=args.scale, reason=args.reason)
                return {"recorded": True}
            if args.command == "backup":
                return {"backup": str(engine.store.backup(args.destination).resolve())}
            if args.command == "prepare":
                text(args.model, "Model", 120)
                invocation, request = engine.start("manual", args.model)
                atomic_write(args.output, json.dumps({"invocation": invocation, **request}, indent=2))
                return {"id": invocation, "request": str(Path(args.output).resolve()),
                        "next": "Paste the request into your desktop model. Save its JSON reply, then run complete."}
            if args.command == "complete":
                require(state["pending"] == args.id and state["invocations"][args.id]["provider"] == "manual",
                        "Only a pending manual invocation can accept a supplied reply")
                require(Path(args.file).stat().st_size <= 256000, "Reply file is too large")
                return engine.finish(args.id, Path(args.file).read_text(), {"identity": "human-attested"})
    finally:
        engine.store.close()
# ---------------------------------------------------------------------------
# STEP: main
#
# Keep this function explicit because it marks a testable boundary in the
# chain from operator/provider input to durable/public output.  Do not fold it
# into a neighboring layer if doing so would hide validation, provenance,
# failure handling, or the distinction between accepted state and a derived view.
# ---------------------------------------------------------------------------


def main():
    args = parser().parse_args()
    try:
        result = execute(args)
        if result is not None:
            print(json.dumps(result, indent=2))
        if isinstance(result, dict) and result.get("status") in ("rejected", "failed"):
            return 2
        return 0
    except (Rejected, IntegrityError, OSError, sqlite3.DatabaseError, ValueError) as exc:
        print(json.dumps({"error": str(exc)}), file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
