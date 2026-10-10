#!/usr/bin/env python3
"""LAN and host-name router for local wake_runner groups."""

import argparse
from html import escape
from http.client import HTTPConnection
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import ipaddress
import json
from pathlib import Path


_HOP_HEADERS = {"connection", "keep-alive", "proxy-authenticate", "proxy-authorization",
                "te", "trailers", "transfer-encoding", "upgrade"}
_MAX_BOB_PACKET = 512_000
_MAX_GROUP_BOB_BYTES = 4_000_000


class GroupProxy(BaseHTTPRequestHandler):
    protocol_version = "HTTP/1.1"

    def do_GET(self):
        self._forward()

    def do_HEAD(self):
        self._forward()

    def _forward(self):
        raw_host = self.headers.get("Host", "").split(":", 1)[0].strip("[]")
        host = raw_host.lower().rstrip(".")
        route = self.server.routes.get(host)
        # The gateway hostname is a presentation alias for the group's canonical
        # prefix. Keep group identity unchanged for peer provenance and routing.
        group = self.server.groups.get(host)
        if group is None:
            for alias_prefix in ("000.", "gateway."):
                if host.startswith(alias_prefix):
                    group = self.server.groups.get(host[len(alias_prefix):])
                    if group is not None:
                        break
        try:
            lan_ip = str(ipaddress.ip_address(raw_host))
        except ValueError:
            lan_ip = None
        if lan_ip is not None:
            if self.path not in {"/", "/index.html"}:
                self.send_error(404, "The group proxy only serves its member directory by IP")
                return
            self._serve_lan_directory(lan_ip)
            return
        if group is not None:
            if not self._allowed(group):
                self.send_error(403, "This host belongs to a different local WAKE group")
                return
            if self.path not in {"/", "/index.html"}:
                self.send_error(404, "The group proxy only serves its member directory")
                return
            self._serve_group_directory(host, group)
            return
        if route is None:
            self.send_error(404, "No grouped WAKE container matches this host")
            return
        if not self._allowed(route):
            self.send_error(403, "This host belongs to a different local WAKE group")
            return
        if self.path.split("?", 1)[0] == "/group/bob.json":
            self._serve_group_bob(route["group_id"])
            return
        try:
            connection = HTTPConnection(route["target"], 8080, timeout=15)
            headers = {key: value for key, value in self.headers.items()
                       if key.lower() not in _HOP_HEADERS and key.lower() != "host"}
            headers["Host"] = self.headers.get("Host", host)
            connection.request(self.command, self.path, headers=headers)
            response = connection.getresponse()
            body = response.read()
            self.send_response(response.status, response.reason)
            for key, value in response.getheaders():
                if key.lower() not in _HOP_HEADERS and key.lower() != "content-length":
                    self.send_header(key, value)
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            if self.command != "HEAD":
                self.wfile.write(body)
            connection.close()
        except (OSError, ValueError):
            self.send_error(502, "Grouped WAKE container is unavailable")

    def _serve_group_bob(self, group_id):
        """Merge published posts from reachable peers; one offline peer is skipped."""
        group = self.server.groups.get(group_id.lower())
        if not group:
            self._json_error(404, "WAKE group is unavailable")
            return
        posts, invocations, evidence, members = {}, {}, {}, []
        for hostname in sorted(group["members"]):
            route = self.server.routes.get(hostname, {})
            target = route.get("target")
            route_group = route.get("group_id", "")
            expected_instance = f"{route_group}-{hostname.split('.', 1)[0]}"
            if not target or route_group.lower() != group_id.lower():
                continue
            connection = None
            try:
                connection = HTTPConnection(target, 8080, timeout=0.6)
                connection.request("GET", "/group/bob.json", headers={"Accept": "application/json"})
                response = connection.getresponse()
                raw = response.read(_MAX_BOB_PACKET + 1)
                if response.status != 200 or len(raw) > _MAX_BOB_PACKET:
                    continue
                packet = json.loads(raw)
                if (not isinstance(packet, dict) or packet.get("schema") != 1
                        or packet.get("group_id") != route_group
                        or packet.get("instance_id") != expected_instance
                        or not isinstance(packet.get("application_head"), str)
                        or len(packet["application_head"]) != 64
                        or not isinstance(packet.get("posts"), list)
                        or not isinstance(packet.get("invocations"), dict)
                        or not isinstance(packet.get("evidence"), dict)):
                    continue
                candidate_posts = dict(posts)
                candidate_invocations = dict(invocations)
                candidate_evidence = dict(evidence)
                for post in packet["posts"]:
                    if isinstance(post, dict) and isinstance(post.get("id"), str):
                        candidate_posts.setdefault(post["id"], post)
                candidate_invocations.update(packet["invocations"])
                candidate_evidence.update(packet["evidence"])
                candidate_size = len(json.dumps({
                    "posts": candidate_posts, "invocations": candidate_invocations,
                    "evidence": candidate_evidence,
                }, separators=(",", ":")).encode("utf-8"))
                if candidate_size > _MAX_GROUP_BOB_BYTES:
                    continue
                posts, invocations, evidence = (
                    candidate_posts, candidate_invocations, candidate_evidence)
                members.append(expected_instance)
            except (OSError, ValueError, TypeError):
                # A stopped, starting, or malformed peer never blocks other members.
                continue
            finally:
                if connection is not None:
                    connection.close()
        if not members:
            self._json_error(503, "No WAKE group member is currently available")
            return
        body = json.dumps({"schema": 1, "group_id": group_id, "available": True,
                           "members": members, "posts": list(posts.values()),
                           "invocations": invocations, "evidence": evidence},
                          separators=(",", ":")).encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Cache-Control", "no-store")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        if self.command != "HEAD":
            self.wfile.write(body)

    def _json_error(self, status, message):
        body = json.dumps({"schema": 1, "available": False, "error": message}).encode()
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Cache-Control", "no-store")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        if self.command != "HEAD":
            self.wfile.write(body)

    def _allowed(self, route):
        try:
            remote = ipaddress.ip_address(self.client_address[0])
            host_gateway = str(remote) == route.get("gateway")
            in_group_network = any(
                remote in ipaddress.ip_network(group["subnet"], strict=False)
                for group in self.server.groups.values()
            )
            local_host = (remote.is_loopback or
                          (remote.is_private and not remote.is_link_local and not in_group_network))
            return (remote in ipaddress.ip_network(route["subnet"], strict=False)
                    or host_gateway or local_host)
        except (KeyError, ValueError):
            return False

    def _serve_group_directory(self, host, group):
        members = sorted(group["members"])
        group_name = members[0].split(".", 1)[1] if members else host
        # Hostname access is the Mac's /etc/hosts path; IP access is routed to
        # _serve_lan_directory below. Docker Desktop rewrites source addresses,
        # so peer-IP comparison cannot reliably distinguish those clients.
        href_for = lambda member: f"http://{member}/console.html"
        description = "Open a member by its local hostname in a new tab."
        panel = self._group_panel(
            group_name,
            members,
            href_for,
            description,
        )
        self._serve_directory(group_name, [panel])

    def _member_runtime(self, member):
        route = self.server.routes.get(member, {})
        connection = None
        try:
            connection = HTTPConnection(route['target'], 8080, timeout=0.7)
            connection.request('GET', '/runtime.json', headers={'Accept': 'application/json'})
            response = connection.getresponse()
            raw = response.read(32_768)
            if response.status != 200:
                raise ValueError('runtime status unavailable')
            packet = json.loads(raw)
            if not isinstance(packet, dict) or packet.get('mode') != 'standalone':
                raise ValueError('unsupported runtime status')
            state = packet.get('state')
            labels = {
                'running': 'Research running',
                'idle': 'Research idle',
                'waiting': 'Waiting for the next research cycle',
                'standby': 'Research paused until midnight Pacific time',
                'paused': 'Research paused',
                'stopped': 'Research stopped',
                'blocked': 'Research blocked',
            }
            if state not in labels:
                raise ValueError('unknown runtime state')
            return state, labels[state]
        except (KeyError, OSError, ValueError, TypeError):
            return 'blocked', 'Container unavailable'
        finally:
            if connection is not None:
                connection.close()

    def _serve_lan_directory(self, lan_ip):
        panels = []
        for group_name, group in sorted(self.server.groups.items()):
            members = [member for member in sorted(group["members"])
                       if self.server.routes[member].get("host_ip") not in {"127.0.0.1", "::1"}]
            if not members:
                panels.append(self._group_panel(
                    group_name, [], lambda member: "",
                    "Recreate this group with LAN publishing enabled to add its links.",
                ))
                continue
            panels.append(self._group_panel(
                group_name,
                members,
                lambda member: (
                    f"http://{lan_ip}:{self.server.routes[member]['host_port']}/console.html"
                ),
                "Open a member on this local network in a new tab.",
            ))
        if not panels:
            self.send_error(403, "No WAKE groups are available from this network")
            return
        self._serve_directory("Local groups", panels)

    def _group_panel(self, group_name, members, href_for, description):
        buttons = "".join(
            self._member_button(member, href_for(member))
            for member in members
        )
        member_count = f"{len(members)} {'member' if len(members) == 1 else 'members'}"
        return (
            '<section class="group-panel" aria-label="Group '
            f'{escape(group_name, quote=True)}">'
            '<header class="group-panel-heading"><div>'
            f'<p class="eyebrow">LOCAL GROUP</p><h2>{escape(group_name)}</h2>'
            f'</div><span class="member-count"><i></i>{member_count}</span></header>'
            f'<p class="group-description">{escape(description)}</p>'
            f'<div class="member-grid">{buttons}</div></section>'
        )

    def _member_button(self, member, href):
        state, label = self._member_runtime(member)
        return (
            '<a class="member-button" '
            f'href="{escape(href, quote=True)}" target="_blank" '
            f'rel="noopener noreferrer" title="{escape(label, quote=True)}" '
            f'aria-label="Open {escape(member, quote=True)} in a new tab · {escape(label, quote=True)}">'
            f'<span>{escape(member.split(".", 1)[0])}</span>'
            f'<span class="member-status-light" data-state="{escape(state, quote=True)}" '
            f'role="img" aria-label="{escape(label, quote=True)}"><i></i></span></a>'
        )

    def _serve_directory(self, title, panels):
        body = (
            '<!doctype html><html lang="en"><head><meta charset="utf-8">'
            '<meta name="viewport" content="width=device-width, initial-scale=1">'
            '<meta name="theme-color" content="#f3f6fb">'
            f'<title>WAKE✳︎ · {escape(title)}</title>'
            '<style>'
            ':root{color-scheme:light;--paper:#e8ecf4;--surface:#f8faff;--ink:#283457;'
            '--muted:#59627e;--line:#c5cce0;--blue:#0f84a5;--violet:#7c5cc4;'
            '--soft:#eef0f8;--button-bg:#f7f9fd;--button-line:#cbd6e9;--button-hover-line:#9eb5dc;'
            '--masthead-bg:rgba(255,255,255,.76);--dot:#75a9d6;--shadow:0 14px 36px rgba(36,40,59,.06)}'
            ':root[data-theme=dark]{color-scheme:dark;--paper:#24283b;--surface:#1f2335;--ink:#c0caf5;'
            '--muted:#a9b1d6;--line:#3b4261;--blue:#7dcfff;--violet:#bb9af7;--soft:#292e42;'
            '--button-bg:#292e42;--button-line:#3b4261;--button-hover-line:#6574a0;'
            '--masthead-bg:rgba(31,35,53,.92);--dot:#7dcfff;--shadow:0 14px 36px rgba(0,0,0,.16)}'
            '*{box-sizing:border-box}body{margin:0;background:var(--paper);color:var(--ink);'
            'font:16px/1.55 Arial,Helvetica,sans-serif;-webkit-font-smoothing:antialiased}'
            'a{color:inherit;text-decoration:none;-webkit-tap-highlight-color:transparent}'
            'a:focus-visible{outline:3px solid var(--violet);outline-offset:4px}'
            '.masthead{height:76px;border-bottom:1px solid var(--line);background:var(--masthead-bg);'
            'display:flex;align-items:center;justify-content:space-between;padding:0 max(22px,calc((100vw - 980px)/2))}'
            '.brand{font-size:25px;line-height:1;font-weight:800;letter-spacing:-1.1px}'
            '.masthead-tools{display:flex;align-items:center;gap:18px}.theme-switch{position:relative;display:inline-flex;'
            'align-items:center;cursor:pointer}.theme-switch input{position:absolute;width:1px;height:1px;margin:0;opacity:0}'
            '.theme-track{display:inline-flex;align-items:center;flex:0 0 34px;width:34px;height:18px;padding:2px;'
            'border:1px solid var(--line);border-radius:20px;background:var(--surface)}'
            '.theme-track i{display:block;width:12px;height:12px;flex:0 0 12px;border-radius:50%;'
            'background:var(--muted);transition:transform .15s ease,background .15s ease}'
            '.theme-switch input:checked+.theme-track i{transform:translateX(16px);background:var(--blue)}'
            '.theme-switch:focus-within{outline:2px solid var(--blue);outline-offset:3px;border-radius:20px}'
            '.brand-star{color:var(--blue);margin-left:2px}.masthead-label,.eyebrow,.member-count,.gateway-foot'
            '{font:10px/1.4 ui-monospace,SFMono-Regular,Consolas,monospace;letter-spacing:.09em;text-transform:uppercase}'
            '.masthead-label{color:var(--muted);display:flex;align-items:center;gap:9px}'
            '.masthead-label i{display:block;width:7px;height:7px;border-radius:50%;background:#e7c35a}'
            'main{width:min(100% - 40px,760px);margin:0 auto;padding:58px 0 64px}'
            '.page-intro{margin-bottom:30px}.eyebrow{color:var(--muted);margin:0 0 9px}'
            'h1{font-size:clamp(30px,6vw,43px);line-height:1.08;letter-spacing:-1.8px;margin:0;font-weight:750}'
            '.intro-copy{color:var(--muted);font-size:14px;margin:12px 0 0;max-width:520px}'
            '.group-list{display:grid;gap:15px}.group-panel{border:1px solid var(--line);border-radius:15px;'
            'background:var(--surface);box-shadow:var(--shadow);padding:21px 22px 22px}'
            '.group-panel-heading{display:flex;align-items:center;justify-content:space-between;gap:12px}'
            '.group-panel-heading .eyebrow{font-size:9px;margin-bottom:5px;color:var(--blue)}'
            '.group-panel h2{font-size:19px;letter-spacing:-.35px;line-height:1.25;margin:0;font-weight:700}'
            '.member-count{display:flex;align-items:center;gap:7px;color:var(--muted);font-size:9px;white-space:nowrap}'
            '.member-count i{width:6px;height:6px;border-radius:50%;background:var(--dot)}'
            '.group-description{color:var(--muted);font-size:12px;margin:11px 0 16px}'
            '.member-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(105px,1fr));gap:9px}'
            '.member-button{min-height:48px;border:1px solid var(--button-line);border-radius:10px;background:var(--button-bg);'
            'display:flex;align-items:center;justify-content:space-between;padding:0 13px;color:var(--blue);'
            'font-size:13px;font-weight:700;transition:background .15s,border-color .15s,transform .15s}'
            '.member-button small{font-size:12px;color:var(--muted);font-weight:400}'
            '.member-status-light{display:inline-flex;align-items:center;justify-content:center;width:12px;height:12px;flex:0 0 12px}'
            '.member-status-light i{display:block;width:10px;height:10px;border-radius:50%;background:#8a96a8}'
            '.member-status-light[data-state=running] i,.member-status-light[data-state=campaign] i{background:#3fb950}'
            '.member-status-light[data-state=paused] i,.member-status-light[data-state=stopped] i,.member-status-light[data-state=waiting] i{background:#e7c35a}'
            '.member-status-light[data-state=idle] i{background:#58a6ff}'
            '.member-status-light[data-state=standby] i{background:#a970ff;box-shadow:0 0 9px rgba(169,112,255,.65)}'
            '.member-status-light[data-state=blocked] i{background:#dc5261}'
            '@media(hover:hover){.member-button:hover{background:var(--soft);border-color:var(--button-hover-line);transform:translateY(-1px)}}'
            '.gateway-foot{margin:23px 0 0;color:var(--muted);font-size:9px;letter-spacing:.04em;text-transform:none}'
            '@media(max-width:480px){.masthead{height:66px;padding:0 17px}.brand{font-size:22px}.masthead-tools{gap:12px}'
            'main{width:calc(100% - 32px);padding:39px 0 48px}.group-panel{padding:18px 16px}'
            '.member-grid{grid-template-columns:repeat(3,minmax(0,1fr));gap:7px}.member-button{padding:0 10px}}'
            '@media(prefers-reduced-motion:reduce){*,*::before,*::after{transition:none!important;scroll-behavior:auto!important}}'
            '</style><script>(function(){let choice;try{choice=localStorage.getItem("wake-site-theme")}catch{}'
            'const dark=choice==="dark"||(!["light","dark"].includes(choice)&&matchMedia("(prefers-color-scheme: dark)").matches);'
            'document.documentElement.dataset.theme=dark?"dark":"light"})();</script></head><body>'
            '<header class="masthead"><div class="brand">WAKE<span class="brand-star">✳︎</span></div>'
            '<div class="masthead-tools"><label class="theme-switch" title="Following system theme">'
            '<input id="theme-toggle" type="checkbox" role="switch" aria-label="Use dark theme">'
            '<span class="theme-track" aria-hidden="true"><i></i></span></label>'
            '<div class="masthead-label"><i></i>LOCAL GATEWAY</div></div></header>'
            '<main><div class="page-intro"><p class="eyebrow">WAKE✳︎ / GROUP ACCESS</p>'
            f'<h1>{escape(title)}</h1>'
            '<p class="intro-copy">Choose a member to open its WAKE Console in a new tab.</p></div>'
            f'<div class="group-list">{"".join(panels)}</div>'
            '<p class="gateway-foot">Each member keeps its own research record and can continue independently.</p>'
            '</main><script>(function(){const root=document.documentElement,media=matchMedia("(prefers-color-scheme: dark)"),'
            'key="wake-site-theme",toggle=document.getElementById("theme-toggle");let choice;'
            'try{choice=localStorage.getItem(key)}catch{}if(!["dark","light"].includes(choice))choice=null;'
            'const sync=()=>{const dark=(choice||(media.matches?"dark":"light"))==="dark",theme=dark?"dark":"light";'
            'root.dataset.theme=theme;root.style.colorScheme=theme;document.querySelector("meta[name=theme-color]").content=dark?"#000000":"#f3f6fb";'
            'toggle.checked=dark;toggle.setAttribute("aria-label",dark?"Use light theme":"Use dark theme");'
            'toggle.closest("label").title=`${choice?"Manual":"Following system"} ${theme} theme · switch to ${dark?"light":"dark"}`};'
            'sync();toggle.addEventListener("change",()=>{choice=toggle.checked?"dark":"light";try{localStorage.setItem(key,choice)}catch{}sync()});'
            'media.addEventListener("change",()=>{if(!choice)sync()});window.addEventListener("storage",event=>{if(event.key===key){'
            'choice=["dark","light"].includes(event.newValue)?event.newValue:null;sync()}})})();</script></body></html>'
        ).encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        if self.command != "HEAD":
            self.wfile.write(body)

    def do_POST(self):
        self.send_error(405, "Group routing is read-only")

    do_PUT = do_POST
    do_PATCH = do_POST
    do_DELETE = do_POST

    def log_message(self, fmt, *args):
        print("000.wake.local: " + fmt % args, flush=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", required=True)
    args = parser.parse_args()
    config = json.loads(Path(args.config).read_text())
    if not isinstance(config, dict):
        raise ValueError("Group route configuration must be an object")
    routes = config.get("routes")
    groups = config.get("groups")
    if not isinstance(routes, dict) or not routes or not isinstance(groups, dict) or not groups:
        raise ValueError("Group route configuration is empty")
    server = ThreadingHTTPServer(("0.0.0.0", 8080), GroupProxy)
    server.routes = routes
    server.groups = groups
    host_lan_ip = config.get("host_lan_ip")
    server.host_lan_ip = str(ipaddress.ip_address(host_lan_ip)) if host_lan_ip else None
    print(f"Local WAKE group router ready for {len(routes)} members in {len(groups)} groups", flush=True)
    server.serve_forever()


if __name__ == "__main__":
    main()
