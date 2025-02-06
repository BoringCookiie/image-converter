from PIL import Image
import os

def convert_image(input_path, output_format, resize=None):
    try:
        img = Image.open(input_path)
        
        if resize:
            img = img.resize(resize)

        filename, _ = os.path.splitext(input_path)
        output_path = f"{filename}.{output_format.lower()}"
        
        img.save(output_path, output_format.upper())
        print(f"✅ Image converted and saved as: {output_path}")
    
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    input_path = input("Enter the image path: ").strip()
    output_format = input("Enter output format (png/jpg/webp): ").strip().lower()
    
    resize_option = input("Resize? (width,height) or press Enter to skip: ").strip()
    resize = tuple(map(int, resize_option.split(','))) if resize_option else None

    convert_image(input_path, output_format, resize)
