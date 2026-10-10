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
        group = self.server.groups.get(host)
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

    def _allowed(self, route):
        try:
            remote = ipaddress.ip_address(self.client_address[0])
            host_gateway = str(remote) == route.get("gateway")
            return (remote in ipaddress.ip_network(route["subnet"], strict=False)
                    or host_gateway or remote.is_loopback)
        except (KeyError, ValueError):
            return False

    def _serve_group_directory(self, host, group):
        links = "".join(
            f'<li><a href="http://{escape(member, quote=True)}/">'
            f'{escape(member)}</a></li>'
            for member in sorted(group["members"])
        )
        self._serve_directory(f"WAKE group {host}", links)

    def _serve_lan_directory(self, lan_ip):
        sections = []
        for group_name, group in sorted(self.server.groups.items()):
            members = [member for member in sorted(group["members"])
                       if self.server.routes[member].get("host_ip") not in {"127.0.0.1", "::1"}]
            if not members:
                sections.append(f"<h2>{escape(group_name)}</h2><p>Recreate this group's containers to enable LAN access.</p>")
                continue
            links = "".join(
                f'<li><a href="http://{escape(lan_ip, quote=True)}:{escape(self.server.routes[member]["host_port"], quote=True)}/console.html">'
                f'{escape(member)}</a></li>'
                for member in members
            )
            sections.append(f"<h2>{escape(group_name)}</h2><ul>{links}</ul>")
        if not sections:
            self.send_error(403, "No WAKE groups are available from this network")
            return
        self._serve_directory("WAKE groups", "".join(sections))

    def _serve_directory(self, title, links):
        body = (
            "<!doctype html><html lang=\"en\"><meta charset=\"utf-8\">"
            f"<title>{escape(title)}</title>"
            f"<h1>{escape(title)}</h1>"
            "<p>Choose a WAKE container:</p>"
            f"{links}</html>"
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
        print("wake.local: " + fmt % args, flush=True)


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
    print(f"Local WAKE group router ready for {len(routes)} members in {len(groups)} groups", flush=True)
    server.serve_forever()


if __name__ == "__main__":
    main()
