# core/metadata.py
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS

def get_decimal_from_dms(dms, ref):
    """Converts Degrees, Minutes, Seconds to Decimal Degrees."""
    try:
        degrees = float(dms[0])
        minutes = float(dms[1])
        seconds = float(dms[2])
        
        # Standard conversion formula
        decimal = degrees + (minutes / 60.0) + (seconds / 3600.0)
        
        # South latitudes and West longitudes are negative
        if ref in ['S', 'W']:
            decimal = -decimal
            
        return round(decimal, 4)
    except Exception:
        return None

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
        exif_data = image._getexif()
        
        if not exif_data:
            return {"Error": "No EXIF metadata found in this image."}

        # Iterate through tags to find Make, Model, and DateTime
        for tag_id, value in exif_data.items():
            tag = TAGS.get(tag_id, tag_id)
            if tag == "Make":
                results["Device"] = str(value)
            elif tag == "Model":
                if results["Device"] != "Unknown":
                    results["Device"] += f" {value}"
                else:
                    results["Device"] = str(value)
            elif tag == "DateTimeOriginal":
                results["Date"] = str(value)

        # Handle GPS Data separately
        gps_info = get_geotagging(exif_data)
        if gps_info and "GPSLatitude" in gps_info and "GPSLongitude" in gps_info:
            lat = get_decimal_from_dms(gps_info["GPSLatitude"], gps_info.get("GPSLatitudeRef", "N"))
            lon = get_decimal_from_dms(gps_info["GPSLongitude"], gps_info.get("GPSLongitudeRef", "E"))
            
            if lat is not None and lon is not None:
                # Format exactly as requested by the project instructions
                results["GPS"] = f"Lat/Lon: ({lat}) / ({lon})"
            else:
                results["GPS"] = "GPS data found but could not be parsed."

        return results

    except Exception as e:
        return {"Error": f"Failed to process image. Details: {e}"}