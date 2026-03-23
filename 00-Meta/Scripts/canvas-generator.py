#!/usr/bin/env python3
import json
import os
import re
from pathlib import Path

VAULT_ROOT = Path("/home/med/Documents/bac/notes")

def generate_id():
    import secrets
    return secrets.token_hex(8)

def find_related_files(concept_path):
    concept_name = concept_path.stem
    # Remove subject prefix if exists (e.g., "Math - ")
    clean_name = re.sub(r'^[^-]+ - ', '', concept_name)
    
    # 1. Find Practice
    practice_files = []
    practice_dir = VAULT_ROOT / "02-Practice"
    # Search recursively for files containing clean_name
    for p in practice_dir.rglob("*.md"):
        if clean_name.lower() in p.name.lower():
            practice_files.append(str(p.relative_to(VAULT_ROOT)))
            
    # 2. Find Extracted
    extracted_files = []
    extracted_dir = VAULT_ROOT / "05-Extracted"
    for p in extracted_dir.rglob("*.md"):
        if clean_name.lower() in p.name.lower():
            extracted_files.append(str(p.relative_to(VAULT_ROOT)))

    # 3. Find Visuals
    visuals = []
    assets_dir = concept_path.parent / "assets"
    if assets_dir.exists():
        for p in assets_dir.glob("*"):
            if p.suffix.lower() in ['.png', '.jpg', '.jpeg', '.svg', '.excalidraw']:
                visuals.append(str(p.relative_to(VAULT_ROOT)))
                
    return practice_files, extracted_files, visuals

def create_canvas(concept_path):
    rel_concept_path = str(concept_path.relative_to(VAULT_ROOT))
    canvas_path = concept_path.with_suffix(".canvas")
    
    practice, extracted, visuals = find_related_files(concept_path)
    
    nodes = []
    edges = []
    
    # Main Concept Node
    concept_id = generate_id()
    nodes.append({
        "id": concept_id,
        "type": "file",
        "file": rel_concept_path,
        "x": 0, "y": 0, "width": 600, "height": 800
    })
    
    # Practice Group
    if practice:
        group_id = generate_id()
        nodes.append({
            "id": group_id, "type": "group", "label": "🎯 Practice",
            "x": 650, "y": 0, "width": 450, "height": 250 * len(practice[:3]) + 50
        })
        for i, p_file in enumerate(practice[:3]): # Limit to 3
            p_id = generate_id()
            nodes.append({
                "id": p_id, "type": "file", "file": p_file,
                "x": 675, "y": 50 + (i * 250), "width": 400, "height": 200
            })
        edges.append({
            "id": generate_id(), "fromNode": concept_id, "toNode": group_id, "fromSide": "right", "toSide": "left"
        })

    # Visuals Group
    if visuals:
        group_id = generate_id()
        nodes.append({
            "id": group_id, "type": "group", "label": "🖼️ Visuals",
            "x": -500, "y": 0, "width": 450, "height": 450
        })
        v_id = generate_id()
        nodes.append({
            "id": v_id, "type": "file", "file": visuals[0], # Just first one for now
            "x": -475, "y": 50, "width": 400, "height": 380
        })
        edges.append({
            "id": generate_id(), "fromNode": concept_id, "toNode": group_id, "fromSide": "left", "toSide": "right"
        })

    # Extracted Group
    if extracted:
        group_id = generate_id()
        nodes.append({
            "id": group_id, "type": "group", "label": "📖 Textbook Context",
            "x": 0, "y": 850, "width": 600, "height": 300
        })
        e_id = generate_id()
        nodes.append({
            "id": e_id, "type": "file", "file": extracted[0],
            "x": 25, "y": 900, "width": 550, "height": 230
        })
        edges.append({
            "id": generate_id(), "fromNode": concept_id, "toNode": group_id, "fromSide": "bottom", "toSide": "top"
        })

    with open(canvas_path, 'w') as f:
        json.dump({"nodes": nodes, "edges": edges}, f, indent=2)
    return canvas_path

if __name__ == "__main__":
    concepts_dir = VAULT_ROOT / "01-Concepts"
    for p in concepts_dir.rglob("*.md"):
        if p.name == "INDEX.md": continue
        print(f"Generating canvas for {p.relative_to(VAULT_ROOT)}...")
        create_canvas(p)

