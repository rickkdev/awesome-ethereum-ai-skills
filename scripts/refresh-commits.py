#!/usr/bin/env python3
"""Refresh README commit dates with authenticated GitHub CLI requests."""

import argparse
import datetime as dt
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile
from urllib.parse import unquote, urlencode, urlsplit


def api(endpoint):
    result = subprocess.run(
        ["gh", "api", "--method", "GET", endpoint], capture_output=True, text=True
    )
    if result.returncode:
        if re.search(r"\bHTTP 404\b", result.stderr):
            return None
        raise RuntimeError(f"GitHub request failed for {endpoint}. Check gh authentication and rate limits.")
    return json.loads(result.stdout)


def github_source(cell):
    for url in re.findall(r"\]\((https?://[^\s)]+)\)", cell):
        parsed = urlsplit(url)
        if parsed.hostname != "github.com":
            continue
        parts = unquote(parsed.path).strip("/").split("/")
        if len(parts) >= 2:
            return "/".join(parts[:2]), parts[2:]
    return None


def refresh(text):
    repositories, commits = {}, {}
    lines = text.splitlines(keepends=True)
    link_index = None
    count = 0
    changed = False
    for index, line in enumerate(lines):
        if not line.startswith("|"):
            link_index = None
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if cells[-1] == "Last GitHub commit":
            if "Link" not in cells:
                raise ValueError("Commit table needs a Link column.")
            link_index = cells.index("Link")
            width = len(cells)
            continue
        if link_index is None or all(re.fullmatch(r":?-+:?", cell) for cell in cells):
            continue
        if len(cells) != width:
            raise ValueError(f"Malformed table row at line {index + 1}.")
        source = github_source(cells[link_index])
        value = "Not verified"
        if source:
            repo, location = source
            if repo not in repositories:
                repositories[repo] = api(f"repos/{repo}")
            metadata = repositories[repo]
            value = "Unavailable"
            if metadata is not None:
                path = ""
                if location:
                    if location[0] not in ("tree", "blob") or len(location) < 2:
                        raise ValueError(f"Use a repository, tree, or blob source link for {repo}.")
                    default_branch = metadata["default_branch"].split("/")
                    remainder = location[1:]
                    if remainder[:len(default_branch)] != default_branch:
                        raise ValueError(f"Use the default branch {metadata['default_branch']} in the source link for {repo}.")
                    path = "/".join(remainder[len(default_branch):])
                key = (repo, path)
                if key not in commits:
                    query = {"per_page": 1, "sha": metadata["default_branch"]}
                    if path:
                        query["path"] = path
                    commits[key] = api(f"repos/{repo}/commits?{urlencode(query)}")
                history = commits[key]
                if history:
                    commit = history[0]
                    date = dt.datetime.fromisoformat(commit["commit"]["committer"]["date"].replace("Z", "+00:00"))
                    day = date.astimezone(dt.timezone.utc).date().isoformat()
                    value = f'[{day}]({commit["html_url"]})'
                if metadata["archived"]:
                    value += "; archived"
        changed = changed or cells[-1] != value
        cells[-1] = value
        lines[index] = "| " + " | ".join(cells) + " |" + ("\n" if line.endswith("\n") else "")
        count += 1
    if not count:
        raise ValueError("No project rows found with a final Last GitHub commit column.")
    updated = "".join(lines)
    today = dt.datetime.now(dt.timezone.utc).date().isoformat()
    marker = f"<!-- commits-checked: {today} -->"
    if re.search(r"<!-- commits-checked: .*? -->", updated):
        updated = re.sub(r"<!-- commits-checked: .*? -->", marker, updated)
    else:
        updated = marker + "\n\n" + updated
    visible = f"Commit metadata checked on {today} (UTC)."
    if re.search(r"Commit metadata checked on (?:\d{4}-\d{2}-\d{2}|pending) \(UTC\)\.", updated):
        updated = re.sub(r"Commit metadata checked on (?:\d{4}-\d{2}-\d{2}|pending) \(UTC\)\.", visible, updated)
    else:
        updated = updated.replace(marker, marker + "\n\n" + visible, 1)
    return updated, count, changed


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Compare against live GitHub without writing.")
    parser.add_argument("--readme", type=Path, default=Path(__file__).resolve().parents[1] / "README.md")
    args = parser.parse_args()
    temporary = None
    try:
        original = args.readme.read_text()
        updated, count, changed = refresh(original)
        if args.check:
            if changed:
                print("GitHub commit columns are out of date. Run without --check to refresh.", file=sys.stderr)
                return 1
        elif original != updated:
            if args.readme.read_text() != original:
                raise RuntimeError("README changed during the refresh. Rerun to preserve those edits.")
            with tempfile.NamedTemporaryFile(mode="w", dir=args.readme.parent, delete=False) as handle:
                temporary = handle.name
                handle.write(updated)
            os.chmod(temporary, args.readme.stat().st_mode)
            os.replace(temporary, args.readme)
            temporary = None
        print(f"Verified {count} project rows against GitHub.")
        return 0
    except (OSError, ValueError, KeyError, TypeError, RuntimeError) as error:
        print(str(error), file=sys.stderr)
        return 2
    finally:
        if temporary:
            os.unlink(temporary)


if __name__ == "__main__":
    sys.exit(main())
