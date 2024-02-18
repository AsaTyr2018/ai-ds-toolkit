import argparse
import os

def calculate_repeat_count(png_count, desired_steps=2000, epochs=10):
    """
    Calculate the number of repeats needed to reach the desired number of steps.
    
    Args:
    png_count (int): Number of PNG files in the folder.
    desired_steps (int): Target total steps for the training (default: 2000).
    epochs (int): Number of epochs for the training (default: 10).
    
    Returns:
    int: Calculated repeat count.
    """
    # Calculate initial number of repeats
    initial_repeats = desired_steps / (png_count * epochs)

    # Round to nearest whole number and adjust according to the rules
    repeats = max(1, round(initial_repeats))
    if repeats > 1:
        repeats += 1  # Increase by 1 if more than 1 repeat is needed

    return repeats

def process_folder_recursive(folder_path):
    print(f"Verarbeite Ordner: {folder_path}")

    # Process the folder and its subfolders
    for root, dirs, files in os.walk(folder_path):
        png_count = len([file for file in files if file.endswith(".png")])
        if png_count > 0:
            subfolder_name = os.path.basename(root)
            repeat_count = calculate_repeat_count(png_count)
            print(f"Ordner: {subfolder_name} - PNGs: {png_count}, Rep: {repeat_count}")

def main():
    # Argument parsing
    parser = argparse.ArgumentParser(description="Berechnet Repeat-Zahlen für Ordner basierend auf der PNG-Anzahl.")
    parser.add_argument("-dir", dest="folder_path", required=True, help="Pfad zum Zielordner")
    args = parser.parse_args()

    # Process the specified folder and its subfolders recursively
    process_folder_recursive(args.folder_path)

if __name__ == "__main__":
    main()
