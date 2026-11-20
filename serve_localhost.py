"""Serve graszp.com and/or vernacular.cloud on localhost for previewing before a push.

Usage (from anywhere):
    python serve_localhost.py                both sites
    python serve_localhost.py graszp         graszp.com only
    python serve_localhost.py vernacular     vernacular.cloud only

    graszp.com        http://localhost:8001/   this repository's folder, as GitHub Pages serves it
    vernacular.cloud  http://localhost:8002/   ../vernacular-cloud-003 (the hand-maintained LLC pages)

The nomenclature (graszp.info) has its own dev server, on port 8899:
    obsidian_to_jsonld\\preview.py or serve_localhost.py

Links between the sites are absolute (https://...), so they lead to the live sites.
The Amplify redirect rules of vernacular.cloud are not imitated here.
"""
import functools
import http.server
import sys
import threading
import time
import webbrowser
from pathlib import Path

HERE = Path(__file__).resolve().parent

# name: (label, folder, port)
SITES = {
    "graszp": ("graszp.com", HERE, 8001),
    "vernacular": ("vernacular.cloud", HERE.parent / "vernacular-cloud-003", 8002),
}


class SiteHandler(http.server.SimpleHTTPRequestHandler):
    # A browser may open a connection and never send a request (Chrome/Edge
    # "preconnect"). Without a timeout the handler waits on it indefinitely.
    timeout = 5
    # Serve markdown (the SAN template) as text, as GitHub Pages does.
    extensions_map = {**http.server.SimpleHTTPRequestHandler.extensions_map,
                      ".md": "text/markdown; charset=utf-8"}


def start(label, folder, port):
    """Start one site's server in a background thread; return it, or None if it can't start."""
    if not folder.is_dir():
        print(f"Error: {label}: folder not found at {folder}")
        return None
    handler = functools.partial(SiteHandler, directory=str(folder))
    try:
        httpd = http.server.ThreadingHTTPServer(("", port), handler)
    except OSError as e:
        print(f"Error: {label}: port {port} is busy ({e}). Is another server already running?")
        return None
    threading.Thread(target=httpd.serve_forever, daemon=True).start()
    return httpd


def main():
    names = sys.argv[1:] or list(SITES)
    unknown = [n for n in names if n not in SITES]
    if unknown:
        print(f"Unknown site: {', '.join(unknown)}. Choose from: {', '.join(SITES)}")
        return

    # On Windows, SO_REUSEADDR would let a second server bind the same port silently.
    http.server.ThreadingHTTPServer.allow_reuse_address = sys.platform != "win32"

    running = []
    print("\n--- graszp.com / vernacular.cloud Dev Server ---")
    for name in names:
        label, folder, port = SITES[name]
        httpd = start(label, folder, port)
        if httpd:
            url = f"http://localhost:{port}/"
            running.append((httpd, url))
            print(f"    {label:<17} {url}   ({folder})")
    if not running:
        return

    print("\n    Press Ctrl+C to stop...")
    for _, url in running:
        webbrowser.open(url)
    try:
        while True:          # a sleep loop, because Ctrl+C can't interrupt Event.wait() on Windows
            time.sleep(0.5)
    except KeyboardInterrupt:
        print("\n--- Server Stopped by User ---")
    finally:
        for httpd, _ in running:
            httpd.shutdown()
            httpd.server_close()


if __name__ == "__main__":
    main()
