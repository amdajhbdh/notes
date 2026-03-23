#!/usr/bin/env python3
import os
import re
from pathlib import Path

VAULT_ROOT = Path("/home/med/Documents/bac/notes")

def fix_links_in_file(file_path):
    try:
        content = file_path.read_text()
    except UnicodeDecodeError:
        return False
        
    # Regex to find links like [[00-Meta/MOCs/Name MOC.md|Label]] or [[00-Meta/MOCs/Name MOC]]
    # We want to simplify them to [[Name MOC]]
    
    # Pattern 1: [[00-Meta/MOCs/Subject MOC.md|Subject MOC]] -> [[Subject MOC]]
    # Pattern 2: [[00-Meta/MOCs/Subject MOC]] -> [[Subject MOC]]
    
    new_content = content
    
    # Generic replacement for 00-Meta/MOCs/ prefix in wikilinks
    # This handles [[00-Meta/MOCs/File.md]] -> [[File]] (stripping extension if present)
    
    def replacer(match):
        full_match = match.group(0)
        link_content = match.group(1)
        
        # Split alias
        if '|' in link_content:
            target, alias = link_content.split('|', 1)
        else:
            target = link_content
            alias = None
            
        # Clean target path
        if "00-Meta/MOCs/" in target:
            clean_target = target.replace("00-Meta/MOCs/", "")
            # Remove .md extension if present
            if clean_target.endswith(".md"):
                clean_target = clean_target[:-3]
            
            if alias:
                return f"[[{clean_target}|{alias}]]"
            else:
                return f"[[{clean_target}]]"
        return full_match

    # Match [[...]] content
    new_content = re.sub(r'\[\[(.*?)\]\]', replacer, new_content)
    
    if new_content != content:
        print(f"Fixing links in {file_path.relative_to(VAULT_ROOT)}")
        file_path.write_text(new_content)
        return True
    return False

if __name__ == "__main__":
    count = 0
    for p in VAULT_ROOT.rglob("*.md"):
        if fix_links_in_file(p):
            count += 1
    print(f"Fixed links in {count} files.")
