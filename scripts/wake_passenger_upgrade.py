#!/usr/bin/env python3
"""Install shared Passenger storage on explicitly selected, paused runner nodes.

Retains the stopped original until the replacement passes health, pause and
authority checks. Never removes volumes; credentials remain in process memory.
"""
import json
import re
import subprocess
import sys
import time

LABEL = "com.sudofx.wake.runner"


def docker(*args):
    result = subprocess.run(["docker", *args], capture_output=True, text=True)
    if result.returncode:
        # Docker error output can contain environment values; do not publish it.
        raise RuntimeError("Docker operation failed; original container retained for recovery")
    return result.stdout.strip()


def inspect(name):
    return json.loads(docker("inspect", name))[0]


def runtime(name, path="runtime.json"):
    return json.loads(docker("exec", name, "python", "-c",
                            "import urllib.request,sys; print(urllib.request.urlopen('http://127.0.0.1:8080/'+sys.argv[1],timeout=5).read().decode())", path))


def configuration(spec, name, owner):
    config, host = spec["Config"], spec["HostConfig"]
    if config["User"] != "10001:10001" or not host["ReadonlyRootfs"] or host.get("Privileged"):
        raise RuntimeError("Unsupported runner security configuration")
    if set(host["PortBindings"]) != {"8080/tcp"} or len(host["PortBindings"]["8080/tcp"]) != 1:
        raise RuntimeError("Unsupported runner port configuration")
    args = ["create", "--name", name, "--user", config["User"], "--workdir", config["WorkingDir"], "--read-only"]
    binding = host["PortBindings"]["8080/tcp"][0]
    args += ["--publish", f"{binding.get('HostIp') or '0.0.0.0'}:{binding.get('HostPort') or '0'}:8080"]
    for key, value in config["Labels"].items():
        args += ["--label", f"{key}={value}"]
    for value in config["Env"]:
        if not value.startswith(("WAKE_PASSENGER_ROOT=", "WAKE_PASSENGER_INSTALLATION=")):
            args += ["--env", value]
    args += ["--env", "WAKE_PASSENGER_ROOT=/passenger", "--env", f"WAKE_PASSENGER_INSTALLATION={owner}"]
    for mount in spec["Mounts"]:
        if mount["Destination"] == "/passenger":
            continue
        if mount["Type"] == "tmpfs":
            continue
        if mount["Type"] not in ("bind", "volume"):
            raise RuntimeError("Unsupported runner mount")
        source = mount.get("Name") if mount["Type"] == "volume" else mount["Source"]
        args += ["--volume", f"{source}:{mount['Destination']}:{'rw' if mount['RW'] else 'ro'}"]
    args += ["--volume", f"{owner}-passenger:/passenger"]
    for path, options in (host.get("Tmpfs") or {}).items():
        args += ["--tmpfs", path + (":" + options if options else "")]
    for flag, field in (("--cap-drop", "CapDrop"), ("--cap-add", "CapAdd"), ("--security-opt", "SecurityOpt")):
        for value in host.get(field) or []:
            args += [flag, value]
    restart = host["RestartPolicy"]["Name"]
    if restart:
        args += ["--restart", restart]
    entry = config.get("Entrypoint") or []
    if entry:
        args += ["--entrypoint", entry[0]]
    networks = list(spec["NetworkSettings"]["Networks"].items())
    if not networks:
        raise RuntimeError("Runner has no network")
    args += ["--network", networks[0][0]]
    for alias in networks[0][1].get("Aliases") or []:
        if not re.fullmatch(r"[a-f0-9]{64}", alias):
            args += ["--network-alias", alias]
    args += [spec["Image"], *entry[1:], *(config.get("Cmd") or [])]
    return args, networks[1:]


def upgrade(name):
    spec = inspect(name)
    labels = spec["Config"]["Labels"]
    if labels.get(LABEL) != "true" or labels.get(LABEL + ".role") not in ("parent", "child"):
        raise RuntimeError("Select a managed parent or child; gateway and unrelated containers are excluded")
    owner = labels.get(LABEL + ".parent") or labels.get(LABEL + ".hostname")
    if not owner or not re.fullmatch(r"[a-zA-Z0-9_.-]{1,100}", owner):
        raise RuntimeError("Missing installation identity")
    if runtime(name)["state"] != "paused":
        raise RuntimeError("Research must be paused before installing storage")
    before = runtime(name, "wake-data.json")
    if before["state"].get("pending"):
        raise RuntimeError("Pending invocation must drain first")
    for mount in spec["Mounts"]:
        if mount["Destination"] == "/passenger":
            if mount.get("Name") != owner + "-passenger":
                raise RuntimeError("Existing Passenger volume has a different installation identity")
            print(f"{name}: shared storage already installed")
            return
    args, networks = configuration(spec, name, owner)
    backup = name + "-passenger-upgrade-backup"
    if docker("ps", "-a", "--filter", "name=^/" + backup + "$", "--format", "{{.Names}}"):
        raise RuntimeError("A recoverable upgrade backup already exists")
    docker("volume", "create", owner + "-passenger")
    docker("run", "--rm", "--user", "0:0", "--entrypoint", "chown", "--volume", owner + "-passenger:/passenger",
           spec["Image"], "10001:10001", "/passenger")
    docker("stop", "--time", "300", name)
    docker("rename", name, backup)
    try:
        docker(*args)
        for network, settings in networks:
            flags = []
            for alias in settings.get("Aliases") or []:
                if not re.fullmatch(r"[a-f0-9]{64}", alias):
                    flags += ["--alias", alias]
            docker("network", "connect", *flags, network, name)
        docker("start", name)
        deadline = time.monotonic() + 90
        while True:
            try:
                after = runtime(name, "wake-data.json")
                if runtime(name)["state"] == "paused" and after["head"] == before["head"]:
                    break
            except RuntimeError:
                pass
            if time.monotonic() >= deadline:
                raise RuntimeError("Replacement failed pause/authority checks")
            time.sleep(.5)
    except Exception:
        if docker("ps", "-a", "--filter", "name=^/" + name + "$", "--format", "{{.Names}}"):
            docker("rm", "-f", name)
        docker("rename", backup, name)
        docker("start", name)
        raise
    docker("rm", backup)
    print(f"{name}: shared storage installed; paused record head preserved")


def main():
    if len(sys.argv) < 2:
        raise RuntimeError("Supply exact managed parent/child container names")
    for name in sys.argv[1:]:
        if not re.fullmatch(r"[A-Za-z0-9_.-]{1,100}", name):
            raise RuntimeError("Invalid container name")
        upgrade(name)
    print("Refresh the existing hostname gateway with scripts/wake_runner --refresh-router.")


if __name__ == '__main__':
    try:
        main()
    except Exception as error:
        print(f"Passenger storage upgrade stopped ({type(error).__name__}). Check the named container and any retained upgrade backup.", file=sys.stderr)
        sys.exit(1)
