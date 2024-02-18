import tkinter as tk
from tkinter import filedialog
import subprocess
import os

def browse_folder(entry):
    """Opens a dialog for folder selection and fills the entry field."""
    folder_path = filedialog.askdirectory()
    entry.delete(0, tk.END)
    entry.insert(0, folder_path)

def convert_videos(input_folder, output_folder):
    """Converts videos to PNG frames."""
    # Ensure the output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Get all video files in the input folder
    video_files = [f for f in os.listdir(input_folder) if f.endswith(('.mp4', '.avi', '.mov', '.mkv'))]  # Extend this list as needed
    for index, video_file in enumerate(video_files, start=1):
        # Create a numbered folder for each video
        video_output_folder = os.path.join(output_folder, f'{index:03d}')
        os.makedirs(video_output_folder, exist_ok=True)
        
        # Execute FFMPEG to extract frames
        video_path = os.path.join(input_folder, video_file)
        command = f'ffmpeg -i "{video_path}" -vf fps=1 "{video_output_folder}/%d.png"'
        subprocess.call(command, shell=True)
        
        print(f'Conversion of {video_file} completed.')

def on_convert():
    """Executed when the user clicks 'Convert'."""
    input_folder = entry_input_folder.get()
    output_folder = entry_output_folder.get()
    label_status.config(text="Please wait...")
    convert_videos(input_folder, output_folder)
    label_status.config(text="Conversion completed!")

# GUI Setup with dark theme
root = tk.Tk()
root.title("Video to PNG Converter")

# Apply dark theme
root.configure(bg="#333333")
style = {"bg": "#333333", "fg": "#ffffff"}

frame = tk.Frame(root, bg="#333333")
frame.pack(padx=10, pady=10)

# Input Folder
tk.Label(frame, text="Input Folder:", **style).grid(row=0, column=0, sticky="w")
entry_input_folder = tk.Entry(frame, width=50)
entry_input_folder.grid(row=0, column=1)
button_input_folder = tk.Button(frame, text="Browse", command=lambda: browse_folder(entry_input_folder), borderwidth=0, highlightthickness=0, bg="#555555", fg="#ffffff")
button_input_folder.grid(row=0, column=2, padx=5, pady=5)

# Output Folder
tk.Label(frame, text="Output Folder:", **style).grid(row=1, column=0, sticky="w")
entry_output_folder = tk.Entry(frame, width=50)
entry_output_folder.grid(row=1, column=1)
button_output_folder = tk.Button(frame, text="Browse", command=lambda: browse_folder(entry_output_folder), borderwidth=0, highlightthickness=0, bg="#555555", fg="#ffffff")
button_output_folder.grid(row=1, column=2, padx=5, pady=5)

# Convert Button
button_convert = tk.Button(frame, text="Convert", command=on_convert, borderwidth=0, highlightthickness=0, bg="#0078D7", fg="#ffffff")
button_convert.grid(row=2, column=1, pady=10)

# Status Label
label_status = tk.Label(frame, text="", **style)
label_status.grid(row=3, column=1)

# Round buttons (requires canvas or image-based approach, here's a simple style adjustment)
button_input_folder.configure(relief=tk.FLAT)
button_output_folder.configure(relief=tk.FLAT)
button_convert.configure(relief=tk.FLAT)

root.mainloop()
