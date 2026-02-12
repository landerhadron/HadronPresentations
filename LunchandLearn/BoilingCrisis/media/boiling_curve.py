from PIL import Image

def extract_plot(input_path, output_path, keep_width, keep_height):
    try:
        img = Image.open(input_path)
        width, height = img.size
        
        # Calculate cut points
        crop_width = int(width * keep_width)
        crop_height = int(height * keep_height)
        
        # Crop (left, top, right, bottom)
        left_crop = img.crop((0, 0, crop_width, crop_height))
        
        left_crop.save(output_path)
        print(f"Success! Saved to {output_path}")
        print(f"Kept top-left portion: {int(keep_width*100)}% width x {int(keep_height*100)}% height")
        
    except Exception as e:
        print(f"Error: {e}")

# --- CONFIGURATION (EDIT HERE) ---
input_filename = 'Boiling-curve-a-adapted-from-Nukiyama-1984-and-Faghri-and-Zhang-2006-and-b-obtained.png'
output_filename = 'extracted_nukiyama_curve.png'

# 0.55 = Keep left 55% of the image (cuts off the right side)
# 1.00 = Keep 100% of the vertical height (no cropping bottom)
MY_WIDTH_RATIO = 0.56  
MY_HEIGHT_RATIO = 0.95

# --- RUN THE CODE ---
extract_plot(input_filename, output_filename, MY_WIDTH_RATIO, MY_HEIGHT_RATIO)
