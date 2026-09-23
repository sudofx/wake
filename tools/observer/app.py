#!/usr/bin/env python3
"""A local, read-only analyst cockpit for WAKE's published durable record."""

from __future__ import annotations

import argparse
import json
import os
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import subprocess
import urllib.error
import urllib.parse
import urllib.request


HERE = Path(__file__).resolve().parent
CONFIG_PATH = HERE / "observer-config.json"


def load_dotenv():
    """Load simple KEY=VALUE entries from this package's local .env file."""
    env_file = HERE / ".env"
    if not env_file.exists():
        return
    for line in env_file.read_text().splitlines():
        if "=" not in line or line.lstrip().startswith("#"):
            continue
        key, value = line.split("=", 1)
        os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))


def configured_source() -> dict | None:
    """Find an explicitly configured checkout without scanning a user's disk."""
    local_candidates = [os.environ.get("WAKE_OBSERVER_WAKE")]
    if CONFIG_PATH.exists():
        try:
            saved = json.loads(CONFIG_PATH.read_text())
            if saved.get("mode") == "github":
                return saved
            local_candidates.append(saved.get("wake_root"))
        except json.JSONDecodeError:
            pass
    local_candidates.extend([str(HERE.parent / "wake"), str(Path.cwd() / "wake")])
    for candidate in local_candidates:
        if candidate and (Path(candidate).expanduser() / ".git").exists():
            return {"mode": "local", "wake_root": str(Path(candidate).expanduser().resolve())}
    repository = os.environ.get("WAKE_OBSERVER_REPOSITORY")
    if repository:
        return {"mode": "github", "repository": repository,
                "branch": os.environ.get("WAKE_OBSERVER_BRANCH", "wake-state")}
    return None


def git(wake_root: Path, *args: str) -> str:
    result = subprocess.run(["git", "-C", str(wake_root), *args], text=True,
                            capture_output=True, check=False)
    if result.returncode:
        raise RuntimeError(result.stderr.strip() or "Could not read the WAKE repository.")
    return result.stdout


def load_live_record(wake_root: Path) -> tuple[dict, list[dict], str]:
    """Fetch only the public state branch, then load its canonical exports."""
    git(wake_root, "fetch", "origin", "wake-state")
    state = json.loads(git(wake_root, "show", "origin/wake-state:state.json"))
    events = [json.loads(line) for line in git(wake_root, "show", "origin/wake-state:events.jsonl").splitlines()]
    head = git(wake_root, "show", "origin/wake-state:head.txt").strip()
    return state, events, head


def load_github_record(repository: str, branch: str) -> tuple[dict, list[dict], str]:
    """Read public WAKE exports from GitHub; no token is required or stored."""
    if not all(part and part.replace("-", "").replace("_", "").isalnum() for part in repository.split("/")) or repository.count("/") != 1:
        raise RuntimeError("GitHub repository must use owner/repository format.")
    ref = urllib.parse.quote(branch, safe="")
    base = f"https://raw.githubusercontent.com/{repository}/{ref}"
    def read(name):
        request = urllib.request.Request(f"{base}/{name}", headers={"User-Agent": "wake-observer-local"})
        with urllib.request.urlopen(request, timeout=20) as response:
            return response.read().decode()
    try:
        state = json.loads(read("state.json"))
        events = [json.loads(line) for line in read("events.jsonl").splitlines()]
        head = read("head.txt").strip()
    except urllib.error.HTTPError as error:
        raise RuntimeError(f"GitHub could not read {repository}@{branch} (HTTP {error.code}).") from error
    return state, events, head


def decision_for(events: list[dict], invocation_id: str) -> dict:
    for event in reversed(events):
        payload = event.get("payload", {})
        if event.get("kind") in {"accepted", "rejected", "deferred", "failed"} and payload.get("id") == invocation_id:
            return event
    return {}


def proposal_outline(decision: dict) -> dict:
    payload = decision.get("payload", {})
    raw = payload.get("raw_response")
    if raw:
        try:
            proposal = json.loads(raw)
        except json.JSONDecodeError:
            proposal = {}
    else:
        proposal = payload.get("proposal", {})
    return {"title": proposal.get("title"), "summary": proposal.get("summary"),
            "actions": [{"type": action.get("type"), "id": action.get("id"),
                         "evidence": action.get("evidence", [])}
                        for action in proposal.get("actions", [])]}


def analyse(state: dict, events: list[dict], head: str) -> dict:
    invocations = state.get("invocations", {})
    if not invocations:
        return {"record": {"version": state.get("version", 0), "head": head, "integrity": "not checked"},
                "latest": None, "pattern": [], "recommendation": "No wake attempts are recorded yet."}
    latest_id, latest = list(invocations.items())[-1]
    decision = decision_for(events, latest_id)
    outcome = latest.get("status", "unknown")
    recent = list(invocations.items())[-12:]
    same_reason = [item for _, item in recent if item.get("reason") and item.get("reason") == latest.get("reason")]
    commitments = [{"id": key, "task": value.get("task"), "due_cycle": value.get("due_cycle")}
                   for key, value in state.get("commitments", {}).items() if value.get("status") == "open"]
    compact = latest.get("trust_compacts_shadow", {}).get("metrics", {})
    retrieval = latest.get("retrieval_shadow", {}).get("metrics", {})
    recommendation = "Inspect the receipt before choosing a next action."
    if outcome == "rejected":
        recommendation = "Do not retry blindly: repair the cited proposal or its governance mismatch first."
    if outcome == "rejected" and len(same_reason) >= 2:
        recommendation = "This is a repeating rejection. Change the proposal inputs or constraint, not just the timing."
    if outcome == "deferred" and len(same_reason) >= 2:
        recommendation = "Provider availability is repeatedly deferring wakes. Treat this separately from governance rejection and retry later rather than changing proposal content without evidence."
    if outcome == "accepted":
        recommendation = "The state advanced. Review the new durable changes and any remaining open commitments."
    provider_history = []
    for invocation_id, item in recent:
        attempts = item.get("provider_attempts", [])
        attempt = attempts[-1] if attempts else {}
        provider_history.append({
            "id": invocation_id,
            "status": item.get("status"),
            "reason": item.get("reason", ""),
            "model": item.get("successful_model") or attempt.get("model") or item.get("model"),
            "http_status": attempt.get("http_status"),
            "result": attempt.get("result"),
            "request_payload_bytes": attempt.get("request_payload_bytes"),
            "provider_category": attempt.get("category"),
            "provider_message": (attempt.get("provider_error") or {}).get("message"),
        })
    return {
        "record": {"version": state.get("version"), "head": head, "event_count": len(events),
                   "integrity": "hash head supplied by wake-state; local reader is read-only"},
        "latest": {"id": latest_id, "status": outcome, "time": latest.get("time"), "finished": latest.get("finished"),
                   "reason": latest.get("reason", ""), "model": latest.get("successful_model") or latest.get("model"),
                   "attempts": latest.get("provider_attempts", []), "proposal": proposal_outline(decision),
                   "trust_compacts": compact, "retrieval": retrieval},
        "pattern": {"recent_attempts": len(recent), "same_reason_count": len(same_reason),
                    "recent_outcomes": [item.get("status") for _, item in recent]},
        "recent_provider_attempts": provider_history,
        "open_commitments": commitments,
        "recommendation": recommendation,
    }


def analyst_prompt(report: dict) -> str:
    """Build a deliberately conservative prompt for the optional outside analyst."""
    rules = (
        "You are a careful outside analyst of WAKE's append-only research record. "
        "Give a concise, non-authoritative opinion about the latest wake. "
        "Separate recorded facts from inference explicitly. Do not invent causal links between independent signals. "
        "A provider deferral (for example HTTP 503/high demand) and a governance rejection are different event classes; "
        "do not combine them into a claim of general system instability unless the supplied record directly supports that link. "
        "Do not infer that request payload size, token count, or model input limits caused a provider error unless the provider "
        "explicitly reports an input-size, token-limit, context-length, or equivalent request-validation error. "
        "When discussing payload size or model behavior, compare recent successful and failed provider attempts from the report "
        "when those observations are available. A successful request of similar magnitude is counterevidence to a simple size claim. "
        "For 503/high-demand responses, describe provider availability as the supported cause unless stronger record evidence exists. "
        "Do not propose bypassing governance. Do not turn correlation into causation. "
        "End with one practical next check that follows from the evidence actually present. "
        "Use plain-text paragraphs only: no Markdown, no headings, and no escaped punctuation.\n\n"
    )
    return rules + json.dumps(report, ensure_ascii=False)


def gemini_opinion(report: dict) -> dict:
    key = os.environ.get("GEMINI_API_KEY")
    if not key:
        raise RuntimeError("Set GEMINI_API_KEY to enable optional AI opinion.")
    model = os.environ.get("WAKE_OBSERVER_GEMINI_MODEL", "gemini-3.1-flash-lite")
    prompt = analyst_prompt(report)
    request = urllib.request.Request(
        f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={key}",
        data=json.dumps({"contents": [{"parts": [{"text": prompt}]}],
                         "generationConfig": {"temperature": 0.2, "maxOutputTokens": 500}}).encode(),
        headers={"Content-Type": "application/json"}, method="POST")
    try:
        with urllib.request.urlopen(request, timeout=45) as response:
            body = json.load(response)
    except urllib.error.HTTPError as error:
        raise RuntimeError(f"Gemini returned HTTP {error.code}.") from error
    candidates = body.get("candidates", [])
    text = "".join(part.get("text", "") for part in candidates[0].get("content", {}).get("parts", [])) if candidates else ""
    if not text:
        raise RuntimeError("Gemini returned no opinion text.")
    return {"model": model, "opinion": text}


class Handler(SimpleHTTPRequestHandler):
    source: dict | None

    def send_json(self, status: int, value: dict):
        body = json.dumps(value, ensure_ascii=False).encode()
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def report(self) -> dict:
        if self.source is None:
            raise RuntimeError("Choose a local WAKE checkout or public GitHub repository below. No data has been read.")
        if self.source["mode"] == "github":
            state, events, head = load_github_record(self.source["repository"], self.source["branch"])
        else:
            state, events, head = load_live_record(Path(self.source["wake_root"]))
        return analyse(state, events, head)

    def do_GET(self):
        if self.path == "/api/report":
            try:
                self.send_json(200, self.report())
            except (RuntimeError, json.JSONDecodeError) as error:
                self.send_json(502, {"error": str(error)})
            return
        return super().do_GET()

    def do_POST(self):
        if self.path == "/api/config":
            try:
                size = int(self.headers.get("Content-Length", "0"))
                supplied = json.loads(self.rfile.read(size))
                if supplied.get("mode") == "github":
                    source = {"mode": "github", "repository": supplied.get("repository", ""),
                              "branch": supplied.get("branch") or "wake-state"}
                    load_github_record(source["repository"], source["branch"])
                else:
                    root = Path(supplied.get("wake_root", "")).expanduser().resolve()
                    if not (root / ".git").exists():
                        raise RuntimeError("That folder is not a Git checkout of WAKE.")
                    source = {"mode": "local", "wake_root": str(root)}
                CONFIG_PATH.write_text(json.dumps(source, indent=2) + "\n")
                type(self).source = source
                self.send_json(200, source)
            except (RuntimeError, json.JSONDecodeError) as error:
                self.send_json(400, {"error": str(error)})
            return
        if self.path != "/api/opinion":
            self.send_error(404)
            return
        try:
            self.send_json(200, gemini_opinion(self.report()))
        except (RuntimeError, json.JSONDecodeError) as error:
            self.send_json(502, {"error": str(error)})


def main():
    load_dotenv()
    parser = argparse.ArgumentParser(description="Run the local WAKE Observer.")
    parser.add_argument("--wake", type=Path, help="Path to a local WAKE checkout")
    parser.add_argument("--port", type=int, default=int(os.environ.get("WAKE_OBSERVER_PORT", "8765")))
    args = parser.parse_args()
    Handler.source = ({"mode": "local", "wake_root": str(args.wake.expanduser().resolve())}
                      if args.wake else configured_source())
    if Handler.source and Handler.source["mode"] == "local" and not Path(Handler.source["wake_root"], ".git").exists():
        raise SystemExit(f"Not a WAKE checkout: {Handler.source['wake_root']}")
    os.chdir(HERE)
    port = args.port
    while port < args.port + 20:
        try:
            server = ThreadingHTTPServer(("127.0.0.1", port), Handler)
            break
        except OSError as error:
            if error.errno != 48:
                raise
            port += 1
    else:
        raise SystemExit(f"No free local port found between {args.port} and {args.port + 19}.")
    print(f"WAKE Observer: http://127.0.0.1:{port}")
    server.serve_forever()


if __name__ == "__main__":
    main()
