#!/usr/bin/env python3
"""
Convert raw OCR text files to proper BAC exam markdown notes with LaTeX.
"""

import os
import re
import sys


def extract_metadata(text, filename):
    """Extract metadata from the first few lines of the raw text."""
    year = 2000
    session = "Normale"
    series = "C"
    subject = "Mathématiques"
    duration = "4 heures"
    coeff = "4"

    text_lower = text[:500].lower()

    # Extract year
    year_match = re.search(r"(\d{4})", text[:200])
    if year_match:
        year = int(year_match.group(1))
    else:
        fname_match = re.search(r"(\d{4})", filename)
        if fname_match:
            year = int(fname_match.group(1))

    # Session
    if "complémentaire" in text_lower or "complementaire" in text_lower:
        session = "Complémentaire"
    elif "session normale" in text_lower or "session de rattrap" in text_lower:
        session = "Normale"
    elif "ratt" in text_lower:
        session = "Rattrapage"
    elif "sc" in filename.lower():
        if "sn" in filename.lower():
            session = "Normale"
        else:
            session = "Complémentaire"
    elif "sn" in filename.lower():
        session = "Normale"

    # Series
    if "tmgm" in text_lower or "tm" in filename.lower():
        series = "TMGM"
    elif "sc" in filename.lower() and "sn" in filename.lower():
        series = "C"  # fallback, filename has both
    elif "c & tmg" in text[:200].lower():
        series = "C & TMGM"
    elif "série c" in text_lower or "serie c" in text_lower:
        series = "C"
    elif "c" in filename.lower():
        series = "C"

    # Subject
    if "mathématiques" in text[:300].lower() or "math" in filename.lower():
        subject = "Mathématiques"
    elif "physique" in text[:300].lower() or "pc" in filename.lower():
        subject = "Physique - Chimie"
    elif "svt" in text[:300].lower() or "sciences naturelles" in text[:300].lower():
        subject = "Sciences Naturelles"

    # Duration
    dur_match = re.search(r"durée[:\s]*(\d+\s*heures?)", text[:300], re.IGNORECASE)
    if dur_match:
        duration = dur_match.group(1)

    # Coefficients
    coeff_match = re.search(r"coefficients?[:\s]*(\d+)", text[:300], re.IGNORECASE)
    if coeff_match:
        coeff = coeff_match.group(1)

    return {
        "year": year,
        "session": session,
        "series": series,
        "subject": subject,
        "duration": duration,
        "coeff": coeff,
    }


def clean_text(text, is_math=False):
    """Clean OCR artifacts and convert to markdown with LaTeX."""
    lines = text.split("\n")
    cleaned = []

    for line in lines:
        # Strip excessive whitespace
        line = line.rstrip()

        # Skip page numbers and headers
        if re.match(r"^\s*([\d/]+\s*)?$", line):
            continue

        # Skip running headers
        if re.match(r"^.*[bB]accalauréat.*\d+[/-]\d+", line):
            continue
        if re.match(r"^.*[aN]nnales.*", line):
            continue

        cleaned.append(line)

    result = "\n".join(cleaned)

    # Convert math notation
    if is_math:
        # Convert common patterns to LaTeX
        result = re.sub(r"\[([^\]]+)\]", r"(\1)", result)  # bracket math
        result = result.replace("∀", r"\forall ")
        result = result.replace("∃", r"\exists ")
        result = result.replace("ℝ", r"\mathbb{R}")
        result = result.replace("ℕ", r"\mathbb{N}")
        result = result.replace("ℤ", r"\mathbb{Z}")
        result = result.replace("ℚ", r"\mathbb{Q}")
        result = result.replace("∈", r"\in ")
        result = result.replace("∉", r"\notin ")
        result = result.replace("⊂", r"\subset ")
        result = result.replace("∑", r"\sum ")
        result = result.replace("∫", r"\int ")
        result = result.replace("∞", r"\infty ")
        result = result.replace("π", r"\pi ")
        result = result.replace("θ", r"\theta ")
        result = result.replace("α", r"\alpha ")
        result = result.replace("β", r"\beta ")
        result = result.replace("→", r"\rightarrow ")
        result = result.replace("⇒", r"\Rightarrow ")
        result = result.replace("≠", r"\neq ")
        result = result.replace("≤", r"\leq ")
        result = result.replace("≥", r"\geq ")
        result = result.replace("²", r"^2")
        result = result.replace("³", r"^3")
        # Convert Unicode superscripts to LaTeX
        superscripts = {
            "⁰": "^{0}",
            "¹": "^{1}",
            "²": "^{2}",
            "³": "^{3}",
            "⁴": "^{4}",
            "⁵": "^{5}",
            "⁶": "^{6}",
            "⁷": "^{7}",
            "⁸": "^{8}",
            "⁹": "^{9}",
        }
        for sup, tex in superscripts.items():
            result = result.replace(sup, tex)
        # Convert Unicode subscripts to LaTeX
        subscripts = {
            "₀": "_{0}",
            "₁": "_{1}",
            "₂": "_{2}",
            "₃": "_{3}",
            "₄": "_{4}",
            "₅": "_{5}",
            "₆": "_{6}",
            "₇": "_{7}",
            "₈": "_{8}",
            "₉": "_{9}",
        }
        for sub, tex in subscripts.items():
            result = result.replace(sub, tex)
        # Fix common OCR artifacts
        result = result.replace("", "[")
        result = result.replace("", "]")
        result = result.replace("", "|")
        result = result.replace("", "}")
        result = result.replace("", "{")
        result = result.replace("", "⊥")
        result = result.replace("", "Δ")
        result = result.replace("", "λ")
        result = result.replace("", "μ")
        result = result.replace("", "π")
        result = result.replace("", "ρ")
        result = result.replace("", "σ")
        result = result.replace("", "τ")
        result = result.replace("", "φ")
        result = result.replace("", "ω")

    return result


def convert_to_markdown(source_path, output_path, is_math=False):
    """Convert a single text file to markdown."""
    with open(source_path, "r", encoding="utf-8", errors="ignore") as f:
        text = f.read()

    basename = os.path.splitext(os.path.basename(source_path))[0]
    filename = basename.replace(".txt", "")

    metadata = extract_metadata(text, filename)
    cleaned = clean_text(text, is_math)

    # Build markdown
    md = []
    md.append("---")
    md.append(
        f'title: "BAC C {metadata["year"]} - Session {metadata["session"]} - {metadata["subject"]}"'
    )
    md.append(f"year: {metadata['year']}")
    md.append(f'exam: "BAC C"')
    md.append(f'session: "{metadata["session"]}"')
    md.append(f'subject: "{metadata["subject"]}"')
    md.append(f'series: "{metadata["series"]}"')
    md.append(f'duration: "{metadata["duration"]}"')
    md.append(f'coefficients: "{metadata["coeff"]}"')
    md.append('type: "Examen"')
    md.append("---")
    md.append("")
    md.append(
        f"# BAC C {metadata['year']} - Session {metadata['session']} - {metadata['subject']}"
    )
    md.append("")
    md.append(
        f"**Série:** {metadata['series']} | **Durée:** {metadata['duration']} | **Coeff:** {metadata['coeff']}"
    )
    md.append("")
    md.append("---")
    md.append("")

    # Split into sections
    sections = re.split(r"\n\s*\n", cleaned)
    for section in sections:
        section = section.strip()
        if not section:
            continue

        # Detect headers
        section_lines = section.split("\n")
        first_line = section_lines[0].strip()

        if any(
            keyword in first_line.lower()
            for keyword in ["exercice", "exercic", "prob", "problème"]
        ):
            # Exercise header
            ex_match = re.match(r"(exercice\s*\d+|problème)", first_line, re.IGNORECASE)
            if ex_match:
                header = ex_match.group(1)
                header = header.title()
                md.append(f"## {header}")
                md.append("")
                for line in section_lines[1:]:
                    if line.strip():
                        md.append(f"*{line.strip()}*")
                md.append("")
            else:
                for line in section_lines:
                    if line.strip():
                        md.append(line)
                md.append("")
        else:
            for line in section_lines:
                if line.strip():
                    md.append(line)
            md.append("")

    md_content = "\n".join(md)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(md_content)

    return basename


def main():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("input_dir")
    parser.add_argument("output_dir")
    parser.add_argument(
        "--math", action="store_true", help="Apply math-specific transformations"
    )
    args = parser.parse_args()

    os.makedirs(args.output_dir, exist_ok=True)

    files = [f for f in os.listdir(args.input_dir) if f.endswith(".txt")]
    files.sort()

    success = 0
    for filename in files:
        source = os.path.join(args.input_dir, filename)
        output_name = filename.replace(".txt", ".md")
        output = os.path.join(args.output_dir, output_name)

        try:
            result = convert_to_markdown(source, output, is_math=args.math)
            success += 1
            print(f"✓ {filename} -> {output_name}")
        except Exception as e:
            print(f"✗ {filename}: {e}")

    print(f"\nDone: {success}/{len(files)} files converted")


if __name__ == "__main__":
    main()
