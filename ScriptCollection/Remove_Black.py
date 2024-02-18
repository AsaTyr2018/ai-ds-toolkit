import os
import argparse
from PIL import Image

def crop_black_borders(image_path, output_path):
    with Image.open(image_path) as img:
        # Convert the image to grayscale to simplify the analysis
        grayscale = img.convert("L")
        # Obtain the pixel values
        pixels = grayscale.load()
        
        # Initialize the boundary values
        left, top, right, bottom = 0, 0, img.width, img.height

        # Define a threshold for black
        threshold = 10  # Depending on your images, you may need to adjust this value

        # Scan from the left
        for x in range(img.width):
            if any(pixels[x, y] > threshold for y in range(img.height)):
                left = x
                break

        # Scan from the right
        for x in range(img.width - 1, -1, -1):
            if any(pixels[x, y] > threshold for y in range(img.height)):
                right = x
                break

        # Scan from the top
        for y in range(img.height):
            if any(pixels[x, y] > threshold for x in range(img.width)):
                top = y
                break

        # Scan from the bottom
        for y in range(img.height - 1, -1, -1):
            if any(pixels[x, y] > threshold for x in range(img.width)):
                bottom = y
                break

        # Crop the image and save it
        cropped_img = img.crop((left, top, right, bottom))
        cropped_img.save(output_path)

def process_directory(directory, output_base):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg')):
                relative_path = os.path.relpath(root, directory)
                output_directory = os.path.join(output_base, relative_path)
                if not os.path.exists(output_directory):
                    os.makedirs(output_directory)
                input_path = os.path.join(root, file)
                output_path = os.path.join(output_directory, file)
                crop_black_borders(input_path, output_path)
                print(f"Processed {input_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Remove black borders from images recursively.")
    parser.add_argument("-dir", "--directory", type=str, required=True, help="Path to the input directory")
    
    args = parser.parse_args()
    input_directory = args.directory
    output_directory = os.path.join(input_directory, "output")

    process_directory(input_directory, output_directory)
