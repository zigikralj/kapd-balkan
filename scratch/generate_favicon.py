import os
from PIL import Image

def generate_favicon():
    # 1. Open the original logo
    img = Image.open('public/logo.png')
    width, height = img.size
    
    # 2. Crop the top graphic section (rows 0 to 215)
    graphic = img.crop((0, 0, width, 216))
    
    # 3. Find the tight bounding box of the non-transparent part of this graphic
    bbox = graphic.getbbox()
    if not bbox:
        print("Error: Bounding box not found in graphic section!")
        return
    
    # Tight crop
    cropped_graphic = graphic.crop(bbox)
    w, h = cropped_graphic.size
    print(f"Tight graphic size: {w}x{h}")
    
    # 4. Make it a square by adding transparent padding
    size = max(w, h)
    square_img = Image.new('RGBA', (size, size), (255, 255, 255, 0))
    # Paste centered
    offset_x = (size - w) // 2
    offset_y = (size - h) // 2
    square_img.paste(cropped_graphic, (offset_x, offset_y))
    
    # 5. Save in various favicon sizes
    # We want a high-res square PNG as public/favicon.png
    square_img.save('public/favicon.png', 'PNG')
    
    # Also save as a multi-size ICO
    # We can save sizes like 16x16, 32x32, 48x48
    # Using Resampling.LANCZOS for resizing
    ico_img = square_img.resize((48, 48), Image.Resampling.LANCZOS)
    ico_img.save('public/favicon.ico', format='ICO', sizes=[(16, 16), (32, 32), (48, 48)])
    
    # Also save as a SVG or SVG backup? Astro's minimal template generated favicon.svg.
    # We can overwrite favicon.svg or just let standard link tags point to favicon.ico/favicon.png.
    print("Favicon files generated successfully!")

if __name__ == '__main__':
    generate_favicon()
