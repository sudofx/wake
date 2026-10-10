#!/usr/bin/env python3
"""Host-name router for local wake_runner groups; listens only behind localhost publish."""

import argparse
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
        host = (self.headers.get("Host", "").split(":", 1)[0]).lower().rstrip(".")
        route = self.server.routes.get(host)
        if route is None:
            self.send_error(404, "No grouped WAKE container matches this host")
            return
        try:
            remote = ipaddress.ip_address(self.client_address[0])
            host_gateway = str(remote) == route.get("gateway")
            if (remote not in ipaddress.ip_network(route["subnet"], strict=False)
                    and not host_gateway and not remote.is_loopback):
                self.send_error(403, "This host belongs to a different local WAKE group")
                return
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

    def do_POST(self):
        self.send_error(405, "Group routing is read-only")

    do_PUT = do_POST
    do_PATCH = do_POST
    do_DELETE = do_POST

    def log_message(self, fmt, *args):
        print("wake-group-router: " + fmt % args, flush=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", required=True)
    args = parser.parse_args()
    routes = json.loads(Path(args.config).read_text())
    if not isinstance(routes, dict) or not routes:
        raise ValueError("Group route configuration is empty")
    server = ThreadingHTTPServer(("0.0.0.0", 8080), GroupProxy)
    server.routes = routes
    print(f"Local WAKE group router ready for {len(routes)} hostnames", flush=True)
    server.serve_forever()


if __name__ == "__main__":
    main()
