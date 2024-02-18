import sys
import subprocess
import argparse
import os

# Precheck for required libraries and ffmpeg
def check_required_libraries():
    try:
        subprocess.run(["ffmpeg", "-version"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except OSError:
        print("ffmpeg is not installed or not in the system's PATH.")
        sys.exit(1)

# Check for argparse and os libraries
try:
    __import__('argparse')
    __import__('os')
except ImportError as e:
    print(f"Missing required Python module: {e.name}")
    sys.exit(1)

def convert_videos(input_folder, output_folder):
    """Converts videos to PNG frames."""
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    video_files = [f for f in os.listdir(input_folder) if f.endswith(('.mp4', '.avi', '.mov', '.mkv'))]
    for index, video_file in enumerate(video_files, start=1):
        video_output_folder = os.path.join(output_folder, f'{index:03d}')
        os.makedirs(video_output_folder, exist_ok=True)

        video_path = os.path.join(input_folder, video_file)
        command = f'ffmpeg -i "{video_path}" -vf fps=1 "{video_output_folder}/%d.png"'
        subprocess.call(command, shell=True)

        print(f'Conversion of {video_file} completed.')

if __name__ == "__main__":
    check_required_libraries()

    parser = argparse.ArgumentParser(description="Convert videos to PNG frames.")
    parser.add_argument("-input", type=str, help="Input folder containing videos.")
    parser.add_argument("-output", type=str, help="Output folder for PNG frames.")

    args = parser.parse_args()

    if args.input and args.output:
        convert_videos(args.input, args.output)
    else:
        print("Input and output folder arguments are required. Use -input <path> and -output <path>.")
