
# 🔍 Image Inspector

An educational digital forensics tool built in Python for analyzing images to extract hidden information, including EXIF metadata and concealed steganographic data.

---

## ⚠️ Disclaimer & Ethical Considerations

**This tool is strictly for educational purposes.**

When using Image Inspector, you must adhere to the following ethical and legal guidelines:
- **Get Permission:** Always obtain explicit, documented permission before analyzing any image that does not belong to you.
- **Respect Privacy:** Metadata (especially GPS coordinates) and hidden messages are highly sensitive. Handle all extracted data responsibly and securely.
- **Follow Laws:** Ensure your activities comply with all local, state, and federal laws regarding data privacy, digital media analysis, and cybersecurity. 
- **No Malicious Use:** The creator of this tool and the institution are not responsible for any misuse of the techniques and scripts demonstrated in this repository.

---

## 📖 Table of Contents
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
  - [Command Line Options](#command-line-options)
  - [Examples](#examples)
- [Project Structure](#project-structure)
- [Testing](#testing)

---

## ✨ Features

1. **Metadata Extraction (`-m`):** Identifies and displays EXIF data, specifically targeting device make/model, original timestamps, and translating raw GPS coordinates into decimal Latitude and Longitude.
2. **Steganography Detection (`-s`):** Scans the image for hidden PGP public key blocks. It utilizes Deep Binary Least Significant Bit (LSB) scanning and End-Of-File (EOF) appended data detection.
3. **Output Management (`-o`):** Securely routes all extracted data to a specified text file for clean reporting and evidence gathering.

---

## 🛠 Prerequisites

To run this tool, you will need:
- **Python 3.7+** installed on your system.
- **Git** (optional, for cloning the repository).

Dependencies are managed via `requirements.txt`. The primary external library used is `Pillow` (Python Imaging Library).

---

## 🚀 Installation

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/yourusername/image-inspector.git](https://github.com/yourusername/image-inspector.git)
   cd image-inspector
   ```

2. **Create and activate a virtual environment (Recommended):**
   - **Linux/macOS:**
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```
   - **Windows:**
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```

3. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

---

## 💻 Usage

Image Inspector is run entirely from the command line.

### Command Line Options

```text
$> python image_inspector.py --help

Welcome to Image Inspector

positional arguments:
  image                 The path to the image file you want to inspect

options:
  -h, --help            show this help message and exit
  -m, --metadata        Extract metadata from the image (e.g., geolocation, device info)
  -s, --steganography   Detect and extract hidden data from the image using steganography techniques
  -o "FileName", --output "FileName"
                        Specify the file name to save output
```

### Examples

**1. Extract Metadata Only**
Prints the device information, date, and decimal GPS coordinates to the terminal.
```bash
python image_inspector.py -m resources/image-example1.jpeg
```

**2. Detect Steganography Only**
Scans for hidden PGP keys and prints them to the terminal.
```bash
python image_inspector.py -s resources/image-example2.jpeg
```

**3. Save Output to a File**
Extracts metadata and saves it directly to `metadata.txt`.
```bash
python image_inspector.py -m -o metadata.txt resources/image-example1.jpeg
```

**4. Combined Analysis**
Runs both the metadata and steganography scans, and saves all findings neatly into a single report file.
```bash
python image_inspector.py -m -s -o forensic_report.txt resources/image-example3.jpeg
```

---

## 📂 Project Structure

```text
image-inspector/
├── README.md                 # Project documentation
├── requirements.txt          # Python dependencies
├── image_inspector.py        # Main entry point script
├── core/                     # Core tool logic
│   ├── cli.py                # Command-line argument parsing and routing
│   ├── metadata.py           # EXIF and GPS extraction math
│   ├── steganography.py      # LSB and EOF extraction algorithms
│   └── file_handler.py       # Output saving and formatting
└── resources/                # Directory containing test images
```

---

## 🧪 Testing

A set of example images is provided in the `resources/` directory to verify the tool's functionality. 
- Some images contain standard EXIF data.
- Some contain hidden steganographic messages.
- Some have had all metadata stripped to test error handling.

To test the robustness of the application, simply run the tool against these images to ensure it does not crash and provides clear feedback to the user.