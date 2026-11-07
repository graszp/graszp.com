"""Release the SAN template from the vault to graszp.com (D-008 / DRY).

The vault note 94.06.01 is the single source and working draft. The site copy
(template/graszp-san-template.md) is a release: it changes only when the
"Template version:" line in the vault note is bumped.

Usage:
    python publish_template.py            check: report whether the site copy is current
    python publish_template.py --publish  copy a new version to the site and update index.html
Then review, commit and push as usual.
"""
import re
import sys
from pathlib import Path

VAULT_TEMPLATE = Path(
    r"C:\Users\joekl\Dropbox\Knowledge Mgt\Personal Knowledge Mgt\00 to 09 Metadata\09 Archive"
    r"\Obsidian Markdown\The Big Picture\90 to 99 Projects\94 Career and Ambition"
    r"\94.06 Solution Architecture portfolio\94.06.01 maintain template for Solution Architecture Note (SAN).md"
)
SITE_DIR = Path(__file__).resolve().parent
SITE_TEMPLATE = SITE_DIR / "template" / "graszp-san-template.md"
INDEX = SITE_DIR / "index.html"

HEADER = (
    "graszp SAN template, from https://graszp.com\n"
    "Licence: CC BY 4.0 (https://creativecommons.org/licenses/by/4.0/). "
    "Credit: graszp.com, Vernacular Cloud LLC.\n\n"
)
VERSION_RE = re.compile(r"Template version:\s*([0-9][0-9.]*)\s*\(([0-9-]+)\)")


def version_of(text):
    m = VERSION_RE.search(text)
    return (m.group(1), m.group(2)) if m else (None, None)


def add_header(body):
    # The template starts with an HTML comment ("<!-- "); the licence goes first inside it.
    first, _, rest = body.partition("\n")
    return f"{first}\n{HEADER}{rest}"


def main():
    publish = "--publish" in sys.argv
    if not VAULT_TEMPLATE.exists():
        sys.exit(f"Vault template not found:\n  {VAULT_TEMPLATE}")
    vault = VAULT_TEMPLATE.read_text(encoding="utf-8")
    site = SITE_TEMPLATE.read_text(encoding="utf-8") if SITE_TEMPLATE.exists() else ""
    v_new, d_new = version_of(vault)
    v_old, _ = version_of(site)
    if not v_new:
        sys.exit("No 'Template version: X.Y (YYYY-MM-DD)' line found in the vault template.")

    wanted = add_header(vault)
    if wanted == site:
        print(f"Up to date: the site has template v{v_new} ({d_new}).")
        return
    if v_new == v_old:
        print(f"The vault template has edits not yet released (both say v{v_new}).")
        print("To release them: bump 'Template version:' in 94.06.01 (new number and date),")
        print("then run: python publish_template.py --publish")
        return
    if not publish:
        print(f"Ready to release: v{v_old} on the site -> v{v_new} ({d_new}) in the vault.")
        print("Run: python publish_template.py --publish")
        return

    SITE_TEMPLATE.parent.mkdir(exist_ok=True)
    SITE_TEMPLATE.write_text(wanted, encoding="utf-8")
    print(f"Copied template v{v_new} to {SITE_TEMPLATE.relative_to(SITE_DIR)}")

    if v_old:
        html = INDEX.read_text(encoding="utf-8")
        n = html.count(f"v{v_old}")
        INDEX.write_text(html.replace(f"v{v_old}", f"v{v_new}"), encoding="utf-8")
        print(f"Updated {n} version mention(s) in index.html: v{v_old} -> v{v_new}")
    print("Also check the 'Updated' date in index.html, then: python serve_localhost.py, commit, push.")


if __name__ == "__main__":
    main()
