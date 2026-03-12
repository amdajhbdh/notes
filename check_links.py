#!/usr/bin/env python3
import os
import re
from pathlib import Path

# Configuration
VAULT_DIR = Path("/home/med/Documents/bac/resources/notes")
# VAULT_DIR = Path(".")  # If we are already in the vault

# Patterns for Obsidian links
WIKILINK_PATTERN = re.compile(r"\[\[([^\]]+)\]\]")
# Markdown links: [text](url)
MD_LINK_PATTERN = re.compile(r"\[([^\]]*)\]\(([^)]+)\)")


def find_markdown_files(root):
    """Find all markdown files in the vault."""
    return list(root.rglob("*.md"))


def resolve_wikilink(link, current_file):
    """Resolve a wikilink to a file path."""
    # Remove any aliases or hash parts
    link = link.split("|")[0].split("#")[0].strip()
    # Try to find the file with .md extension
    # First, in the same directory
    same_dir = current_file.parent / f"{link}.md"
    if same_dir.exists():
        return same_dir
    # Then, recursively in the vault
    for md_file in VAULT_DIR.rglob(f"{link}.md"):
        return md_file
    # If not found, return None
    return None


def resolve_md_link(link, current_file):
    """Resolve a markdown link to a file path."""
    # Remove any hash parts
    link = link.split("#")[0].strip()
    # If it's a relative path, resolve it relative to the current file
    if not os.path.isabs(link):
        resolved = (current_file.parent / link).resolve()
        # Check if the resolved path exists
        if resolved.exists():
            return resolved
        # If not, try adding .md if it's missing
        if not resolved.suffix:
            resolved_with_md = resolved.with_suffix(".md")
            if resolved_with_md.exists():
                return resolved_with_md
    else:
        # Absolute path
        if os.path.exists(link):
            return Path(link)
        # Try adding .md
        if not Path(link).suffix:
            link_with_md = link + ".md"
            if os.path.exists(link_with_md):
                return Path(link_with_md)
    return None


def check_file_links(file_path):
    """Check all links in a markdown file."""
    broken = []
    try:
        content = file_path.read_text(encoding="utf-8")
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return broken

    # Find wikilinks
    for match in WIKILINK_PATTERN.finditer(content):
        link_text = match.group(1)
        resolved = resolve_wikilink(link_text, file_path)
        if not resolved:
            broken.append(("wikilink", link_text, str(file_path)))

    # Find markdown links
    for match in MD_LINK_PATTERN.finditer(content):
        # We only care about links that point to files (not URLs)
        link_url = match.group(2)
        # Skip if it's a web URL
        if link_url.startswith("http://") or link_url.startswith("https://"):
            continue
        resolved = resolve_md_link(link_url, file_path)
        if not resolved:
            broken.append(("mdlink", link_url, str(file_path)))

    return broken


def main():
    print("Scanning for markdown files...")
    md_files = find_markdown_files(VAULT_DIR)
    print(f"Found {len(md_files)} markdown files.")

    all_broken = []
    for md_file in md_files:
        broken = check_file_links(md_file)
        if broken:
            all_broken.extend(broken)

    if all_broken:
        print("\nBroken links found:")
        for link_type, link_text, file_path in all_broken:
            print(f"{file_path}: {link_type} -> '{link_text}'")
    else:
        print("\nNo broken links found.")


if __name__ == "__main__":
    main()
