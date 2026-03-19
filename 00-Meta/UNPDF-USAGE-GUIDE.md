---
date: {{date:YYYY-MM-DD}}
tags: meta, guide, pdf-extraction
---

# 📄 unpdf Usage Guide

**Date:** {{date:YYYY-MM-DD HH:mm}}

## Overview

The `unpdf` crate is now integrated into your OCR system for high-performance PDF content extraction.

## Installation

The crate is already added to your workspace:
- **Workspace:** `Cargo.toml` - `unpdf = "0.2"`
- **OCR Crate:** `crates/ocr/Cargo.toml` - `unpdf.workspace = true`

## Available Tools

### 1. CLI Tools

#### extract-pdf
Extract text from a single PDF file:

```bash
# Extract as plain text (default)
cargo run --bin extract-pdf -- document.pdf

# Extract as Markdown
cargo run --bin extract-pdf -- document.pdf markdown
```

#### batch-extract
Extract text from all PDFs in a directory:

```bash
# Extract all PDFs in a directory
cargo run --bin batch-extract -- /path/to/pdfs

# Extract as Markdown
cargo run --bin batch-extract -- /path/to/pdfs markdown
```

### 2. Library API

#### Basic Extraction

```rust
use bac_ocr::{extract_text_from_pdf, pdf_to_markdown};

// Extract plain text
let text = extract_text_from_pdf("document.pdf")?;

// Extract as Markdown
let markdown = pdf_to_markdown("document.pdf")?;
```

#### Async Processing

```rust
use bac_ocr::{process_pdf, process_pdf_to_markdown};

// Extract text asynchronously
let text = process_pdf("document.pdf").await?;

// Extract Markdown asynchronously
let markdown = process_pdf_to_markdown("document.pdf").await?;
```

#### Validation and Detection

```rust
use bac_ocr::{validate_pdf, detect_pdf_format};

// Check if file is a valid PDF
if validate_pdf("document.pdf") {
    println!("Valid PDF");
}

// Detect PDF format
let format = detect_pdf_format("document.pdf")?;
println!("PDF format: {:?}", format);
```

## Features

### Multiple Output Formats
- **Markdown:** Structured content with headings, lists, tables
- **Plain Text:** Clean text with cleanup pipeline
- **JSON:** Structured data (planned)

### Structure Preservation
- Headings (H1-H6)
- Paragraphs and text blocks
- Tables (with fallback modes)
- Lists (ordered/unordered)
- Images (extracted to directory)

### Text Cleanup
- Normalization for LLM training
- Multiple cleanup presets:
  - `Standard`: Basic cleanup
  - `Aggressive`: Extensive cleanup
  - `Minimal`: Minimal changes

### Page Selection
- Extract all pages
- Extract specific page range
- Extract specific pages

### Table Handling
- **Markdown:** Standard Markdown tables
- **HTML:** HTML table tags
- **ASCII:** ASCII art tables

## Configuration

### ExtractionConfig

```rust
use bac_ocr::{ExtractionConfig, OutputFormat, CleanupPreset, TableFallback};

let config = ExtractionConfig {
    format: OutputFormat::Markdown,
    extract_images: false,
    image_dir: None,
    include_frontmatter: false,
    max_heading_level: 6,
    preserve_line_breaks: true,
    line_width: 0,
    collect_stats: false,
    page_selection: PageSelection::All,
    cleanup_preset: CleanupPreset::Standard,
    table_fallback: TableFallback::Markdown,
};
```

## Practical Examples

### Extract PDFs from Resources Folder

```bash
# Run the extraction script
./scripts/extract-resources.sh
```

This will:
1. Scan `03-Resources/` for PDF files
2. Extract text to `05-Extracted/Resources/`
3. Save as Markdown files

### Process a Specific PDF

```bash
# Extract a textbook PDF
cargo run --bin extract-pdf -- "03-Resources/CHI-7AS-C.pdf" markdown

# Extract exam paper
cargo run --bin extract-pdf -- "04-Exams/BAC-2020.pdf" markdown
```

### Batch Process All PDFs

```bash
# Extract all PDFs in a directory
cargo run --bin batch-extract -- "03-Resources" markdown

# Extract exam papers
cargo run --bin batch-extract -- "04-Exams" markdown
```

## Integration with Vault

### Automatic Extraction

1. **Resources Folder:** `03-Resources/` → `05-Extracted/Resources/`
2. **Exams Folder:** `04-Exams/` → `05-Extracted/Exams/`
3. **Daily Notes:** Attach PDFs to daily notes

### Linking Extracted Content

After extraction, link to concept notes:

```markdown
# Extracted Content from PDF

← Back to [[Chemistry MOC]]

## Key Concepts
- [Concept 1]
- [Concept 2]

## Related Notes
- [[Acids and Bases]]
- [[Titration]]
```

## Performance Tips

1. **Parallel Processing:** `unpdf` uses Rayon for multi-page documents
2. **Memory Efficient:** Stream processing for large PDFs
3. **Cleanup Pipeline:** Use `CleanupPreset::Aggressive` for LLM training

## Troubleshooting

### Issue: PDF not recognized
**Solution:** Check file extension and use `validate_pdf()` to verify

### Issue: Poor text extraction
**Solution:** Try different cleanup presets or table fallback modes

### Issue: Large PDFs timeout
**Solution:** Use page selection to extract specific pages

## Examples from Your Vault

### Extract Chemistry Textbook

```bash
# Extract chemistry textbook
cargo run --bin extract-pdf -- "03-Resources/CHI-7AS-C.pdf" markdown

# Output: 05-Extracted/Resources/CHI-7AS-C.md
```

### Extract Exam Papers

```bash
# Extract all exam papers
cargo run --bin batch-extract -- "04-Exams" markdown

# Output: 05-Extracted/Exams/*.md
```

## API Reference

### Functions

| Function | Description | Returns |
|----------|-------------|---------|
| `validate_pdf()` | Check if file is valid PDF | `bool` |
| `detect_pdf_format()` | Detect PDF format | `PdfFormat` |
| `extract_text_from_pdf()` | Extract plain text | `String` |
| `pdf_to_markdown()` | Convert to Markdown | `String` |
| `pdf_to_text()` | Convert to plain text | `String` |
| `process_pdf()` | Async text extraction | `Result<String>` |
| `process_pdf_to_markdown()` | Async Markdown conversion | `Result<String>` |

### Configuration

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `format` | `OutputFormat` | `Markdown` | Output format |
| `extract_images` | `bool` | `false` | Extract images |
| `include_frontmatter` | `bool` | `false` | Add YAML frontmatter |
| `max_heading_level` | `u8` | `6` | Max heading level |
| `preserve_line_breaks` | `bool` | `true` | Keep line breaks |
| `line_width` | `u32` | `0` | Line wrapping (0 = none) |
| `collect_stats` | `bool` | `false` | Collect extraction stats |
| `cleanup_preset` | `CleanupPreset` | `Standard` | Text cleanup level |
| `table_fallback` | `TableFallback` | `Markdown` | Table rendering mode |

---

*Start extracting your PDFs today! 🚀*