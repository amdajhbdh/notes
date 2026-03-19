---
date: {{date:YYYY-MM-DD}}
tags: meta, guide, image-extraction, pdf
---

# 🖼️ Image Extraction Guide

**Date:** {{date:YYYY-MM-DD HH:mm}}

## Overview

Your OCR system now supports image extraction from PDFs and standalone image processing.

## Tools Available

### 1. extract-images
Extract images from PDF files or process standalone images:

```bash
# Extract images from PDF
cargo run --bin extract-images -- document.pdf images/ pdf

# Process standalone images
cargo run --bin extract-images -- /path/to/images /path/to/output standalone
```

### 2. extract-pdf (Enhanced)
Now supports image extraction via configuration:

```bash
# Extract PDF with images
cargo run --bin extract-pdf -- document.pdf markdown
```

## Image Extraction from PDFs

### Basic Usage

```bash
# Extract images from a PDF
cargo run --bin extract-images -- "03-Resources/CHI-7AS-C.pdf" "07-Assets/extracted-images" pdf
```

This will:
1. Extract all images from the PDF
2. Save them to the specified directory
3. Return a list of extracted image paths

### Configuration

You can configure image extraction in the `ExtractionConfig`:

```rust
use bac_ocr::{ExtractionConfig, ImageFormat};

let config = ExtractionConfig {
    extract_images: true,
    image_dir: Some(PathBuf::from("images/")),
    image_format: ImageFormat::PNG,  // PNG, JPEG, WebP, or Original
    image_quality: 85,               // 0-100 for lossy formats
    ..Default::default()
};
```

### Image Formats

| Format | Description | Best For |
|--------|-------------|----------|
| `PNG` | Lossless compression | Diagrams, charts, text |
| `JPEG` | Lossy compression | Photographs |
| `WebP` | Modern format | Web optimization |
| `Original` | Keep original format | Preserve quality |

## Standalone Image Processing

### Basic Usage

```bash
# Process images in a directory
cargo run --bin extract-images -- /path/to/images /path/to/output standalone
```

This will:
1. Scan directory for image files (PNG, JPG, GIF, BMP, WebP, SVG)
2. Copy/process them to output directory
3. Return list of processed images

### Supported Formats

- **PNG** - Portable Network Graphics
- **JPG/JPEG** - Joint Photographic Experts Group
- **GIF** - Graphics Interchange Format
- **BMP** - Bitmap Image
- **WebP** - Web Picture format
- **SVG** - Scalable Vector Graphics

## Integration with Vault

### Extract Images from Resources

```bash
# Extract images from chemistry textbook
cargo run --bin extract-images -- "03-Resources/CHI-7AS-C.pdf" "07-Assets/extracted-images/CHI-7AS-C" pdf

# Extract images from exam papers
cargo run --bin extract-images -- "04-Exams/BAC-2020.pdf" "07-Assets/extracted-images/exams" pdf
```

### Process Standalone Images

```bash
# Process images from a folder
cargo run --bin extract-images -- "07-Assets/raw-images" "07-Assets/processed-images" standalone
```

### Link Images in Notes

After extraction, link images in your notes:

```markdown
# Chemistry Notes

## Diagrams

![Molecular Structure](07-Assets/extracted-images/CHI-7AS-C/page1_molecule.png)

## Equations

![Reaction Diagram](07-Assets/extracted-images/CHI-7AS-C/page2_reaction.png)
```

## Advanced Usage

### Extract with Text and Images

```bash
# Extract text and images together
cargo run --bin extract-pdf -- "document.pdf" markdown

# Images are saved to configured directory
# Text references images in Markdown
```

### Batch Image Extraction

```bash
# Extract images from multiple PDFs
for pdf in 03-Resources/*.pdf; do
    cargo run --bin extract-images -- "$pdf" "07-Assets/extracted-images" pdf
done
```

### Image Quality Control

```rust
// High quality for printing
let config = ExtractionConfig {
    image_quality: 95,
    ..Default::default()
};

// Web optimized
let config = ExtractionConfig {
    image_quality: 75,
    ..Default::default()
};
```

## API Reference

### Functions

| Function | Description | Returns |
|----------|-------------|---------|
| `extract_images_from_pdf()` | Extract images from PDF | `Vec<PathBuf>` |
| `process_standalone_images()` | Process standalone images | `Vec<PathBuf>` |

### Configuration

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `extract_images` | `bool` | `false` | Enable image extraction |
| `image_dir` | `Option<PathBuf>` | `None` | Output directory for images |
| `image_format` | `ImageFormat` | `Original` | Output image format |
| `image_quality` | `u8` | `85` | Image quality (0-100) |

## Examples from Your Vault

### Extract Chemistry Diagrams

```bash
# Extract all images from chemistry textbook
cargo run --bin extract-images -- "03-Resources/CHI-7AS-C.pdf" "07-Assets/chemistry-diagrams" pdf
```

### Process Exam Graphs

```bash
# Extract graphs from exam papers
cargo run --bin extract-images -- "04-Exams/BAC-2020.pdf" "07-Assets/exam-graphs" pdf
```

### Organize Extracted Images

```bash
# Create organized structure
mkdir -p 07-Assets/extracted/{chemistry,physics,biology,exams}

# Extract by subject
cargo run --bin extract-images -- "03-Resources/CHI-7AS-C.pdf" "07-Assets/extracted/chemistry" pdf
cargo run --bin extract-images -- "03-Resources/PHY-7D.pdf" "07-Assets/extracted/physics" pdf
```

## Troubleshooting

### Issue: No images extracted
**Solution:** PDF might not contain embedded images or images are scanned

### Issue: Poor image quality
**Solution:** Increase `image_quality` or use `ImageFormat::Original`

### Issue: Large image files
**Solution:** Use JPEG format with lower quality for smaller files

### Issue: SVG not supported
**Solution:** SVG is supported for standalone images, but PDF extraction may not support SVG

## Performance Tips

1. **Batch extraction** - Process multiple PDFs in parallel
2. **Quality vs size** - Balance image quality with file size
3. **Format selection** - Use PNG for diagrams, JPEG for photos
4. **Organize early** - Create organized directories before extraction

## Next Steps

1. **Extract images** from your chemistry textbook
2. **Process diagrams** from exam papers
3. **Link images** in your concept notes
4. **Create visual** study materials

---

*Start extracting images today! 🖼️*