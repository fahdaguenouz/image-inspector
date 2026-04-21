# core/cli.py
import argparse
from core.metadata import extract_metadata
from core.metadata import extract_metadata
from core.steganography import extract_hidden_data
def main():
    # Initialize the parser with a custom description
    parser = argparse.ArgumentParser(
        prog="image-inspector",
        description="Welcome to Image Inspector",
        formatter_class=argparse.RawTextHelpFormatter
    )

    # Define the optional arguments (flags)
    parser.add_argument(
        '-m', '--metadata',
        action='store_true', # Stores True if the flag is present
        help="Extract metadata from the image (e.g., geolocation, device info)"
    )
    
    parser.add_argument(
        '-s', '--steganography',
        action='store_true',
        help="Detect and extract hidden data from the image using steganography techniques"
    )
    
    parser.add_argument(
        '-o', '--output',
        type=str,
        metavar='FileName',
        help="Specify the file name to save output"
    )

    # Define the positional argument for the target image
    parser.add_argument(
        'image',
        type=str,
        help="The path to the image file you want to inspect"
    )

    # Parse the arguments from the user's terminal input
    args = parser.parse_args()

    # --- Skeleton Logic Routing ---
    
    if not args.metadata and not args.steganography:
        print("[-] No action specified. Use -m for metadata or -s for steganography.")
        print("[-] Run 'python image_inspector.py --help' for more information.")
        return 1

    if args.metadata:
        print(f"[*] Extracting metadata from '{args.image}'...\n")
        metadata_results = extract_metadata(args.image)
        
        for key, value in metadata_results.items():
            print(f"{key}: {value}")
        print("-" * 30)
        
    if args.steganography:
        print(f"[*] Searching for hidden data in '{args.image}' (This may take a moment)...\n")
        steg_results = extract_hidden_data(args.image)
        
        for key, value in steg_results.items():
            print(f"{value}") # Just print the value to keep the PGP key format clean
        print("-" * 30)
        
    if args.output:
        print(f"[*] Results will be saved to '{args.output}'")
        # TODO: Route the extracted data to core/file_handler.py to save it

    return 0