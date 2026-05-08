from PIL import Image

def text_to_bin(text, lsb_first=False):
    """Converts a string to its binary representation."""
    if lsb_first:
        # Reverses the bits in each byte for LSB-first encoding
        return ''.join(format(ord(c), '08b')[::-1] for c in text)
    return ''.join(format(ord(c), '08b') for c in text)

def bin_to_text(binary):
    """Converts a perfectly aligned binary string to text."""
    text = ""
    for i in range(0, len(binary), 8):
        byte = binary[i:i+8]
        if len(byte) == 8:
            text += chr(int(byte, 2))
    return text

def extract_hidden_data(image_path):
    """
    Performs a deep scan for hidden PGP keys using EOF extraction 
    and robust binary-level LSB scanning.
    """
    try:
        # 1. FILE HEX / EOF CHECK (Very common for JPEG images)
        with open(image_path, 'rb') as f:
            content = f.read()
            # JPEG EOF marker is FFD9
            eof_marker = b'\xff\xd9'
            if eof_marker in content:
                # Grab everything appended after the official end of the image
                eof_data = content.split(eof_marker)[-1]
                if b"-----BEGIN PGP" in eof_data:
                    start = eof_data.find(b"-----BEGIN PGP")
                    end = eof_data.find(b"-----END PGP PUBLIC KEY BLOCK-----")
                    if start != -1 and end != -1:
                        # Extract and decode the raw bytes
                        pgp_key = eof_data[start:end + 34].decode('utf-8', errors='ignore')
                        return {"Hidden Data (EOF Appended)": pgp_key}

        # 2. DEEP BINARY LSB SCAN
        image = Image.open(image_path)
        image = image.convert('RGB')
        pixels = list(image.getdata())

        # Extract the LSB from every R, G, B channel
        bit_string = "".join([str(value & 1) for pixel in pixels for value in pixel[:3]])

        pgp_start = "-----BEGIN PGP PUBLIC KEY BLOCK-----"
        pgp_end = "-----END PGP PUBLIC KEY BLOCK-----"

        # Try both Standard (MSB-first) and Reversed (LSB-first) bit packing
        for lsb_first in [False, True]:
            start_bin = text_to_bin(pgp_start, lsb_first)
            end_bin = text_to_bin(pgp_end, lsb_first)

            # Search for the exact binary signature (ignores byte alignment issues)
            start_idx = bit_string.find(start_bin)
            
            if start_idx != -1:
                end_idx = bit_string.find(end_bin, start_idx)
                if end_idx != -1:
                    # We found the binary block! Slice it out exactly.
                    key_bin = bit_string[start_idx:end_idx + len(end_bin)]
                    
                    # Convert the isolated binary block back to text
                    if lsb_first:
                        pgp_key = "".join([chr(int(key_bin[i:i+8][::-1], 2)) for i in range(0, len(key_bin), 8)])
                    else:
                        pgp_key = bin_to_text(key_bin)
                        
                    return {"Hidden Data (LSB Extracted)": pgp_key}
                else:
                    return {"Warning": "Found PGP start header in binary, but no end header."}

        return {"Result": "No hidden PGP key detected using LSB or EOF techniques."}

    except Exception as e:
        return {"Error": f"Steganography analysis failed: {e}"}