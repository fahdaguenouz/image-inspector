# core/metadata.py
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS

def get_geotagging(exif):
    """Extracts GPS data from the EXIF dictionary."""
    if not exif:
        return None

    geotagging = {}
    for (key, val) in exif.items():
        if key in TAGS and TAGS[key] == 'GPSInfo':
            for (t, v) in val.items():
                sub_decoded = GPSTAGS.get(t, t)
                geotagging[sub_decoded] = v
            break
    return geotagging

def extract_metadata(image_path):
    """Extracts device info, date, and GPS data from an image."""
    results = {
        "Device": "Unknown",
        "Date": "Unknown",
        "GPS": "No GPS data found"
    }
    
    try:
        image = Image.open(image_path)
        # _getexif() extracts the raw metadata
        exif_data = image._getexif()
        
        if not exif_data:
            return {"Error": "No EXIF metadata found in this image."}

        # Iterate through tags to find Make, Model, and DateTime
        for tag_id, value in exif_data.items():
            tag = TAGS.get(tag_id, tag_id)
            if tag == "Make":
                results["Device"] = str(value)
            elif tag == "Model":
                # Append model to the Make if it exists
                if results["Device"] != "Unknown":
                    results["Device"] += f" {value}"
                else:
                    results["Device"] = str(value)
            elif tag == "DateTimeOriginal":
                results["Date"] = str(value)

        # Handle GPS Data separately
        gps_info = get_geotagging(exif_data)
        if gps_info:
            results["GPS"] = f"Raw GPS Data: {gps_info}" 
            # Note: For the actual latitude/longitude float conversion, 
            # you will need to parse the Degrees/Minutes/Seconds math.

        return results

    except Exception as e:
        return {"Error": f"Failed to process image. Details: {e}"}