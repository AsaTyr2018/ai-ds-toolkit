from PIL import Image
import os
import math
import argparse

parser = argparse.ArgumentParser(description="Create a Collage Image.")
parser.add_argument('-dir', '--directory', type=str, help='Path to the Images', required=True)
args = parser.parse_args()

input_folder = args.directory

image_files = [f for f in os.listdir(input_folder) if f.endswith(".jpg") or f.endswith(".png")]

num_images = len(image_files)

image = Image.open(os.path.join(input_folder, image_files[0]))
image_width, image_height = image.size

num_images_per_col = int(math.sqrt(num_images))
num_images_per_row = math.ceil(num_images / num_images_per_col)

collage_width = num_images_per_row * image_width
collage_height = num_images_per_col * image_height

collage = Image.new("RGB", (collage_width, collage_height))

for i, image_file in enumerate(image_files):
    img = Image.open(os.path.join(input_folder, image_file))
    
    x_position = (i % num_images_per_row) * image_width
    y_position = (i // num_images_per_row) * image_height
    collage.paste(img, (x_position, y_position))

collage.save("collage.png")

print(f"Image created")
