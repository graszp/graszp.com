"""Serve graszp.com on localhost for previewing before a push.

Usage (from anywhere):  python serve_localhost.py [port]
Serves the folder this script sits in (the repo root), as GitHub Pages does.
Default port 8001, so it can run alongside the vernacular.cloud dev server.
"""
import functools
import http.server
import sys
import webbrowser
from pathlib import Path

SITE_DIR = Path(__file__).resolve().parent
PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8001


class SiteHandler(http.server.SimpleHTTPRequestHandler):
    # A browser may open a connection and never send a request (Chrome/Edge
    # "preconnect"). Without a timeout the handler waits on it indefinitely.
    timeout = 5
    # Serve markdown (the SAN template) as text, as GitHub Pages does.
    extensions_map = {**http.server.SimpleHTTPRequestHandler.extensions_map,
                      ".md": "text/markdown; charset=utf-8"}


def serve():
    handler = functools.partial(SiteHandler, directory=str(SITE_DIR))
    # On Windows, SO_REUSEADDR would let a second server bind the same port silently.
    http.server.ThreadingHTTPServer.allow_reuse_address = sys.platform != "win32"
    try:
        httpd = http.server.ThreadingHTTPServer(("", PORT), handler)
    except OSError as e:
        print(f"Error: port {PORT} is busy ({e}). Try: python serve_localhost.py {PORT + 1}")
        return

    url = f"http://localhost:{PORT}/"
    with httpd:
        print("\n--- graszp.com Dev Server ---")
        print(f"    Home:  {url}")
        print(f"    Root:  {SITE_DIR}")
        print("\n    Press Ctrl+C to stop...")
        webbrowser.open(url)
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n--- Server Stopped by User ---")


if __name__ == "__main__":
    serve()
