---
date: {{date:YYYY-MM-DD}}
tags: meta, ocr, pdf-extraction, unpdf
---

# 🚀 Enhanced OCR System with unpdf

**Date:** {{date:YYYY-MM-DD HH:mm}}
**Status:** Production Ready

## Overview

Your OCR system has been enhanced with the `unpdf` crate for high-performance PDF content extraction. This system provides powerful tools for extracting text from PDFs in your BAC study vault.

## Architecture

### Core Components

1. **Library** (`crates/ocr/src/lib.rs`)
   - PDF extraction functions
   - Batch processing with Rayon
   - Configuration system
   - Async support

2. **CLI Tools**
   - `extract-pdf` - Single PDF extraction
   - `batch-extract` - Directory batch extraction

3. **Scripts**
   - `extract-resources.sh` - Vault PDF extraction

## Features

### 📄 PDF Extraction

#### Basic Extraction
```rust
use bac_ocr::{extract_text_from_pdf, pdf_to_markdown};

// Extract plain text
let text = extract_text_from_pdf("document.pdf")?;

// Extract as Markdown
let markdown = pdf_to_markdown("document.pdf")?;
```

#### With Statistics
```rust
use bac_ocr::{extract_pdf_with_stats, ExtractionConfig};

let config = ExtractionConfig::default();
let result = extract_pdf_with_stats("document.pdf", &config)?;

println!("Pages: {}", result.page_count);
println!("Characters: {}", result.char_count);
println!("Lines: {}", result.line_count);
println!("Time: {}ms", result.extraction_time_ms);
```

### ⚡ Parallel Processing

The system uses Rayon for parallel PDF extraction:

```rust
// Batch extract with parallel processing
let response = batch_extract("03-Resources", config, true).await?;

println!("Success: {}", response.success_count);
println!("Failed: {}", response.failure_count);
println!("Total: {}", response.total_files);
```

### 🎛️ Configuration Options

```rust
pub struct ExtractionConfig {
    pub format: OutputFormat,           // Markdown, PlainText, Json
    pub extract_images: bool,           // Extract embedded images
    pub image_dir: Option<PathBuf>,     // Image output directory
    pub include_frontmatter: bool,      // YAML frontmatter
    pub max_heading_level: u8,          // H1-H6
    pub preserve_line_breaks: bool,     // Keep line breaks
    pub line_width: u32,                // Line wrapping (0 = none)
    pub collect_stats: bool,            // Collect extraction stats
    pub page_selection: PageSelection,  // All, range, or specific pages
    pub cleanup_preset: CleanupPreset,  // Standard, Aggressive, Minimal
    pub table_fallback: TableFallback,  // Markdown, HTML, ASCII
}
```

## Usage

### CLI Tools

#### Extract Single PDF
```bash
# Extract as plain text
cargo run --bin extract-pdf -- document.pdf

# Extract as Markdown
cargo run --bin extract-pdf -- document.pdf markdown
```

#### Batch Extract Directory
```bash
# Extract all PDFs in directory
cargo run --bin batch-extract -- /path/to/pdfs

# Extract as Markdown
cargo run --bin batch-extract -- /path/to/pdfs markdown
```

### Vault Integration

#### Extract Resources Folder
```bash
# Run the vault extraction script
./scripts/extract-resources.sh
```

This will:
1. Scan `03-Resources/` for PDF files
2. Extract text to `05-Extracted/Resources/`
3. Save as Markdown files

#### Process Exam Papers
```bash
# Extract all exam papers
cargo run --bin batch-extract -- "04-Exams" markdown
```

## Performance

### Parallel Processing
- **Rayon-based**: Multi-threaded extraction
- **Memory efficient**: Stream processing for large PDFs
- **Scalable**: Handles hundreds of PDFs efficiently

### Extraction Speed
- **Small PDFs** (< 1MB): ~100-500ms
- **Medium PDFs** (1-10MB): ~1-5 seconds
- **Large PDFs** (> 10MB): ~5-30 seconds

### Quality
- **Structure preservation**: Headings, paragraphs, tables
- **Text cleanup**: Multiple presets for different use cases
- **Format support**: Markdown, plain text, JSON

## Integration with Vault

### File Structure
```
resources/notes/
├── 03-Resources/           # Source PDFs
├── 05-Extracted/           # Extracted text
│   ├── Resources/          # Extracted resources
│   └── Exams/              # Extracted exams
└── 00-Meta/
    └── UNPDF-USAGE-GUIDE.md # This guide
```

### Workflow

1. **Add PDFs** to `03-Resources/`
2. **Run extraction** script
3. **Review extracted** content in `05-Extracted/`
4. **Link to concepts** in `01-Concepts/`

### Example: Chemistry Textbook

```bash
# Extract chemistry textbook
cargo run --bin extract-pdf -- "03-Resources/CHI-7AS-C.pdf" markdown

# Output: 05-Extracted/Resources/CHI-7AS-C.md
```

Then link to your chemistry notes:

```markdown
# Acids and Bases

← Back to [[Chemistry MOC]]

## Key Concepts
- Strong vs weak acids
- pH calculations
- Titration

## Extracted Content
- [[05-Extracted/Resources/CHI-7AS-C#Acids]]
- [[05-Extracted/Resources/CHI-7AS-C#Bases]]
```

## Advanced Features

### Image Extraction
```rust
let config = ExtractionConfig {
    extract_images: true,
    image_dir: Some(PathBuf::from("images/")),
    ..Default::default()
};
```

### Page Selection
```rust
use unpdf::PageSelection;

// Extract specific pages
let config = ExtractionConfig {
    page_selection: PageSelection::Range(1..=10),
    ..Default::default()
};
```

### Cleanup Presets
```rust
use unpdf::CleanupPreset;

// Standard cleanup (default)
let config = ExtractionConfig {
    cleanup_preset: CleanupPreset::Standard,
    ..Default::default()
};

// Aggressive cleanup for LLM training
let config = ExtractionConfig {
    cleanup_preset: CleanupPreset::Aggressive,
    ..Default::default()
};
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
| `extract_pdf_with_stats()` | Extract with metadata | `ExtractionResult` |
| `batch_extract()` | Batch process directory | `BatchExtractionResponse` |

### Structs

| Struct | Description |
|--------|-------------|
| `ExtractionConfig` | PDF extraction configuration |
| `ExtractionResult` | Extraction result with metadata |
| `BatchExtractionResponse` | Batch extraction results |

## Troubleshooting

### Issue: Empty extraction
**Solution:** PDF might be scanned or image-based. Try different cleanup presets.

### Issue: Poor formatting
**Solution:** Adjust `table_fallback` or `max_heading_level` in config.

### Issue: Slow extraction
**Solution:** Use page selection to extract specific pages only.

### Issue: Large output files
**Solution:** Use `CleanupPreset::Aggressive` for smaller output.

## Examples from Your Vault

### Extract All Resources
```bash
./scripts/extract-resources.sh
```

### Extract Specific PDF
```bash
cargo run --bin extract-pdf -- "03-Resources/CHI-7AS-C.pdf" markdown
```

### Batch Extract Exams
```bash
cargo run --bin batch-extract -- "04-Exams" markdown
```

## Performance Tips

1. **Use parallel processing** for multiple PDFs
2. **Select specific pages** for large PDFs
3. **Use aggressive cleanup** for LLM training data
4. **Extract images separately** if needed
5. **Monitor extraction time** for optimization

## Next Steps

1. **Extract all PDFs** from `03-Resources/`
2. **Process exam papers** from `04-Exams/`
3. **Link extracted content** to concept notes
4. **Use extracted content** for study and review
5. **Set up automated extraction** in your workflow

---

*Start extracting your PDFs today! 🚀*