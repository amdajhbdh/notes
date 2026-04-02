#!/usr/bin/env python3
"""
Simple script to convert OCR math exam text to markdown using direct line numbers.
"""

import re
from pathlib import Path


def process_ocr_to_markdown():
    """Process OCR text and create markdown files."""

    input_file = Path(
        "/home/med/Documents/bac/notes/05-Extracted/OCR/mauritanian-bac/mathematiques/baccmaths_2000_2012.txt"
    )
    output_dir = Path("/home/med/Documents/bac/notes/04-Exams/BAC-2002-2012")

    # Read the OCR file
    with open(input_file, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()

    # Exam sections - line numbers (1-indexed based on the OCR file)
    exams = [
        ("2012", "Normal", 179, 327),
        ("2012", "Complementaire", 340, 451),
        ("2011", "Normal", 464, 594),
        ("2011", "Complementaire", 600, 750),
        ("2010", "Normal", 762, 866),
        ("2010", "Complementaire", 877, 990),
        ("2011", "Normal", 997, 1107),
        ("2009", "Complementaire", 1116, 1218),
        ("2008", "Normal", 1234, 1329),
        ("2008", "Complementaire", 1341, 1480),
        ("2007", "Normal", 1494, 1642),
        ("2007", "Complementaire", 1655, 1819),
        ("2006", "Normal", 1828, 1993),
        ("2006", "Complementaire", 2004, 2147),
        ("2005", "Normal", 2158, 2316),
        ("2005", "Complementaire", 2327, 2471),
        ("2004", "Normal", 2485, 2646),
        ("2004", "Complementaire", 2653, 2749),
        ("2003", "Normal", 2762, 2909),
        ("2003", "Complementaire", 2922, 3017),
        ("2002", "Normal", 3029, 3132),
        ("2002", "Complementaire", 3141, 3248),
    ]

    print(f"Processing {len(exams)} exam sessions...")

    lines = content.split("\n")
    created_files = []

    for year, session, start_line, end_line in exams:
        # Skip if we already have a file with this year/session
        session_short = "N" if session == "Normal" else "C"

        # Extract content (adjust for 0-indexing)
        exam_lines = lines[start_line - 1 : end_line - 1]
        exam_content = "\n".join(exam_lines)

        # Clean up
        exam_content = clean_content(exam_content)

        # Create markdown
        markdown = create_markdown(year, session, exam_content)

        # Write file
        filename = f"BAC-{year}-{session_short}.md"
        output_path = output_dir / filename
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(markdown)

        created_files.append(filename)
        print(f"Created: {filename}")

    return created_files


def clean_content(text):
    """Clean up OCR text."""

    lines = text.split("\n")
    cleaned = []
    skip_until_exercise = True

    for line in lines:
        line = line.strip()

        # Skip header junk
        if skip_until_exercise:
            if "Exercice" in line or "Problème" in line:
                skip_until_exercise = False
                cleaned.append(line)
        else:
            if line:
                cleaned.append(line)

    result = "\n".join(cleaned)

    # Convert exercise headers
    result = re.sub(
        r"Exercice\s*(\d+)\s*\((\d+\s*points?)\)", r"## Exercice \1 (\2)", result
    )
    result = re.sub(r"Probl[èe]me\s*\((\d+)\s*points?\)", r"## Problème (\1)", result)

    # Clean newlines
    result = re.sub(r"\n\n\n+", "\n\n", result)

    return result


def create_markdown(year, session, content):
    """Create markdown with frontmatter."""

    session_norm = "Normale" if session == "Normal" else "Complémentaire"

    return f"""---
tags: [bac, mauritania, {year}, {session.lower()}-session, mathematics, exam, serie-C, serie-TMGM]
year: {year}
session: {session_norm}
subjects: [mathematics]
duration: 4h
coefficients: 9/6
---

# BAC {year} - Session {session_norm} - Mathématiques

**Série:** C & TMGM  
**Durée:** 4 heures  
**Coefficients:** 9 (série C) / 6 (série TMGM)

---

{content}

---

## Tags

#bac #mauritania #mathematics #series-C #series-TMGM #examen

**Source:** Institut Pédagogique National (IPN) - Mauritanie - Edition 2013
"""


if __name__ == "__main__":
    created = process_ocr_to_markdown()
    print(f"\nTotal files created: {len(created)}")
