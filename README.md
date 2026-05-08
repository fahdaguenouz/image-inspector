
# Image Inspector

Image Inspector is a Python-based forensic utility designed to extract embedded information from image files. It provides two core functionalities: extracting EXIF metadata (device information, date, and GPS coordinates) and detecting hidden data using steganographic techniques (EOF scanning and LSB analysis).

## Features

* **Metadata Extraction:** Automatically parses EXIF data to recover device make/model, timestamps, and GPS coordinates (converted to decimal degrees).
* **Steganography Detection:**
* **EOF Scanning:** Detects data appended after the end-of-file (EOF) marker (e.g., JPEG `FFD9`).
* **Binary LSB Scanning:** Deep-scans the Least Significant Bits of pixel data to find hidden patterns or PGP keys, supporting both standard and LSB-first bit packing.


* **Flexible Output:** Results can be printed directly to the terminal or saved to a specified text file.

## Prerequisites

Ensure you have Python 3.x installed. This project relies on the **Pillow** library for image processing.

Install the dependency:

```bash
pip install Pillow

```

## Usage

The tool is a command-line interface (CLI). Run it from your terminal using the following flags:

```bash
python image_inspector.py [options] <path_to_image>

```

### Options

| Flag | Description |
| --- | --- |
| `-m`, `--metadata` | Extract EXIF metadata (Device, Date, GPS). |
| `-s`, `--steganography` | Search for hidden PGP keys/data. |
| `-o`, `--output` | Specify a filename to save the results. |

### Examples

**Extract metadata and print to terminal:**

```bash
python image_inspector.py -m photo.jpg

```

**Search for hidden data and save to a file:**

```bash
python image_inspector.py -s -o results.txt photo.jpg

```

**Run all analyses and save to a file:**

```bash
python image_inspector.py -m -s -o analysis_report.txt photo.jpg

```

## Project Structure

* `image_inspector.py`: The entry point for the application.
* `core/cli.py`: Handles command-line arguments and logic routing.
* `core/metadata.py`: Logic for parsing and calculating EXIF data.
* `core/steganography.py`: Algorithms for detecting hidden binary data.
* `core/file_handler.py`: Utility for formatting and saving extracted data.

## Disclaimer

This tool is intended for educational and forensic analysis purposes only. Please ensure you have authorization before analyzing images that do not belong to you or for which you do not have permission to inspect.