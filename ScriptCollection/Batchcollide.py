import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import os
import math
from PIL import Image

# Function to create a collage
def create_collage(directory):
    image_files = [f for f in os.listdir(directory) if f.endswith(".jpg") or f.endswith(".png")]
    num_images = len(image_files)
    if num_images == 0:
        messagebox.showinfo("No Images Found", "No .jpg or .png files found in the selected directory.")
        return

    image = Image.open(os.path.join(directory, image_files[0]))
    image_width, image_height = image.size
    num_images_per_col = int(math.sqrt(num_images))
    num_images_per_row = math.ceil(num_images / num_images_per_col)
    collage_width = num_images_per_row * image_width
    collage_height = num_images_per_col * image_height
    collage = Image.new("RGB", (collage_width, collage_height))

    for i, image_file in enumerate(image_files):
        img = Image.open(os.path.join(directory, image_file))
        x_position = (i % num_images_per_row) * image_width
        y_position = (i // num_images_per_row) * image_height
        collage.paste(img, (x_position, y_position))

    collage.save(os.path.join(directory, "collage.png"))
    messagebox.showinfo("Collage Created", "Collage image created successfully in the selected directory.")

# Function to calculate repeats
def calculate_repeat_count(png_count, desired_steps=2000, epochs=10):
    initial_repeats = desired_steps / (png_count * epochs)
    repeats = max(1, round(initial_repeats))
    if repeats > 1:
        repeats += 1
    return repeats

def process_folder_for_png_count(directory):
    png_count = 0
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.png'):
                png_count += 1
    return png_count

def on_calculate_repeats_click():
    global root
    directory = filedialog.askdirectory()
    if directory:
        results_window = tk.Toplevel(root)
        results_window.title("Berechnete Repeats")
        text_area = tk.Text(results_window, wrap="word")
        text_area.pack(expand=True, fill="both")

        for root, dirs, files in os.walk(directory):
            png_count = sum(1 for file in files if file.endswith('.png'))
            if png_count > 0:
                repeats = calculate_repeat_count(png_count)
                text_area.insert(tk.END, f"Ordner: {root}, PNG-Anzahl: {png_count}, Repeats: {repeats}\n")

        text_area.configure(state="disabled")

# Function to add tags
def add_tags_to_files(root_folder):
    for root, dirs, files in os.walk(root_folder):
        for file in files:
            if file.endswith('.txt'):
                file_path = os.path.join(root, file)
                character_folder = os.path.basename(root)
                main_folder_name = os.path.basename(os.path.dirname(root))

                with open(file_path, 'r') as f:
                    lines = f.readlines()

                with open(file_path, 'w') as f:
                    for line in lines:
                        tags = line.split(', ')
                        tags.insert(0, character_folder)
                        tags.insert(0, main_folder_name)
                        tags = [tag.strip() for tag in tags]
                        new_line = ', '.join(tags)
                        f.write(new_line)

def on_add_tags_click():
    directory = filedialog.askdirectory()
    if directory:
        add_tags_to_files(directory)
        messagebox.showinfo("Tags Added", "Tags added to .txt files in the selected directory.")

# Function to handle button click for creating collage
def on_create_collage_click():
    directory = filedialog.askdirectory()
    if directory:
        create_collage(directory)

# GUI-Einstellungen
root = tk.Tk()
root.title("Image Processing Tools")
root.geometry("400x200")  # Fenstergröße anpassen

# Stil-Einstellungen
button_font = ("Arial", 12)
button_bg = "#4f4f4f"
button_fg = "white"

# Button-Definitionen mit Stil
create_collage_button = tk.Button(root, text="Create Collage", command=on_create_collage_click, font=button_font, bg=button_bg, fg=button_fg)
calculate_repeats_button = tk.Button(root, text="Calculate Repeats", command=on_calculate_repeats_click, font=button_font, bg=button_bg, fg=button_fg)
add_tags_button = tk.Button(root, text="Add Tags", command=on_add_tags_click, font=button_font, bg=button_bg, fg=button_fg)

# Button-Platzierungen mit Padding
create_collage_button.pack(pady=10)
calculate_repeats_button.pack(pady=10)
add_tags_button.pack(pady=10)

root.mainloop()
