# tests for image_inspector core functionality

import pytest
from pathlib import Path

from core.metadata import extract_metadata
from core.steganography import extract_hidden_data

# Helper to get resource image path
def resource_path(filename: str) -> Path:
    return Path(__file__).resolve().parents[1] / "resources" / filename

# ---------------------- Metadata Tests ----------------------

def test_metadata_image_example1():
    img = resource_path("image-example1.jpeg")
    result = extract_metadata(str(img))
    # Expected GPS string as per project output
    expected_gps = "Lat/Lon: (32.0866) / (34.8851)"
    assert result.get("GPS") == expected_gps
    # Device and Date may be unknown for this sample
    assert result.get("Device") == "Unknown"
    assert result.get("Date") == "Unknown"

def test_metadata_image_example2_no_exif():
    img = resource_path("image-example2.jpeg")
    result = extract_metadata(str(img))
    assert "Error" in result
    assert result["Error"] == "No EXIF metadata found in this image."

def test_metadata_no_data_image():
    img = resource_path("no-data.jpeg")
    result = extract_metadata(str(img))
    assert "Error" in result
    assert result["Error"] == "No EXIF metadata found in this image."

def test_metadata_invalid_path():
    # Pass a directory path instead of a file
    dir_path = resource_path("")
    result = extract_metadata(str(dir_path))
    assert "Error" in result
    # The exact error message may vary, ensure it mentions failure
    assert "Failed to process image" in result["Error"]

# ---------------------- Steganography Tests ----------------------

def test_steg_image_example1_hidden_data():
    img = resource_path("image-example1.jpeg")
    result = extract_hidden_data(str(img))
    # Should detect hidden data either via EOF or LSB
    assert any(key.startswith("Hidden Data") for key in result.keys())
    # Ensure the extracted data starts with PGP block header
    hidden = next(iter(result.values()))
    assert hidden.strip().startswith("-----BEGIN PGP PUBLIC KEY BLOCK-----")

def test_steg_image_example2_hidden_data():
    img = resource_path("image-example2.jpeg")
    result = extract_hidden_data(str(img))
    assert any(key.startswith("Hidden Data") for key in result.keys())
    hidden = next(iter(result.values()))
    assert hidden.strip().startswith("-----BEGIN PGP PUBLIC KEY BLOCK-----")

def test_steg_no_data_image():
    img = resource_path("no-data.jpeg")
    result = extract_hidden_data(str(img))
    # Expect the generic no hidden data result
    assert result.get("Result") == "No hidden PGP key detected using LSB or EOF techniques."

def test_steg_invalid_path():
    # Pass a non-existent file
    img_path = resource_path("nonexistent.jpeg")
    result = extract_hidden_data(str(img_path))
    assert "Error" in result
    assert "Steganography analysis failed" in result["Error"]
