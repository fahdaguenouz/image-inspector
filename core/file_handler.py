import os

def save_results(results, output_path, analysis_type):
    """
    Saves extracted dictionary data to a text file.
    Appends to the file if it already exists.
    """
    try:
        # Open in append mode ('a') with utf-8 encoding for PGP characters
        with open(output_path, 'a', encoding='utf-8') as f:
            for key, value in results.items():
                # If it's a PGP key, just print the raw value without the key name
                if "Hidden Data" in key:
                    f.write(f"{value}\n")
                else:
                    f.write(f"{key}: {value}\n")
            f.write("\n") # Add a blank line for readability
        return True
    except Exception as e:
        print(f"[-] Error writing to {output_path}: {e}")
        return False