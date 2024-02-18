# Python to your Aid!

Today, I am delighted to introduce a suite of open-source Python tools aimed at enhancing your dataset creation workflow. These tools are designed for ease of use and efficiency, offering a range of functionalities to streamline your tasks.

## Tools Overview

### 1. Collage Creator

This simple yet effective tool generates a checkerboard pattern collage from images within a specified folder. To utilize it, execute the following command in your command prompt:

```bash
python collage.py -dir "Path to the folder"
```

The collage is saved in the script's directory for convenient access.

### 2. Steps Calculator

Based on my hands-on experience, this utility calculates an advisable repetition count for your projects, considering a set of images and established parameters. Default settings recommend 10 epochs or roughly 2000 steps. Implement it using:

```bash
python repcalc.py -dir "Path to the Dataset"
```

It's important to remember that these recommendations are starting points and may need adjustment through experimentation.

### 3. Tag Replacer

Facilitate the batch modification of tags within your dataset with this script. Directly modify the script to set the folder path on line 23 (note the need to double backslashes in Python paths), and define the old and new tags on lines 24 and 25, respectively. Run it with:

```bash
python TagReplace.py
```

### New 4. Combined GUI for Tools 1-3

I've enhanced the usability of the first three tools by integrating them into a single, user-friendly graphical interface. Simply launch it with:

```bash
python Batchcollide.py
```

### New 5. Remove_Black

A utility designed to efficiently remove black borders from images, streamlining the cleanup process across multiple folders. Before running, ensure Python and Pillow are installed, then execute:

```bash
python Remove_Black.py -dir "path/to/your/pictures"
```

It processes and saves the adjusted images in a new "output" folder within the original directory.

### New 6. Screencapper

This advanced addition, featuring a tkinter-based GUI, allows for converting videos into frames. It supports custom FPS and quality settings, utilizing ffmpeg for the conversion process. Required installations include Python, ffmpeg, and ffprobe. Start with:

```bash
python screencapper.py
```

#### Update screencapperv2

The tool, named "ScreenCapperV2," is a user-friendly application designed for creating datasets through screen captures. It allows users to convert videos into PNG frames at a rate of one frame per second, facilitating the generation of visual data for various projects. This update includes a graphical user interface for easy folder selection and status updates, making it accessible for users without technical expertise.

```bash
python screencapperv2.py
```

### New Tool: ScreenCapper-CLI

Building on the foundation laid by `ScreenCapperV2`, the `ScreenCapper-CLI` is a streamlined, command-line interface (CLI) tool designed for Linux users. It enables the conversion of videos into PNG frames without the need for a graphical user interface, making it ideal for automated workflows or for use on servers.

To utilize this tool, navigate to your toolset directory and execute the following command:

```bash
python3 ./screencapper-cli.py -input "path/to/your/videos" -output "path/to/save/frames"
```

#### Options:

- `-h, --help` Show this help message and exit.
- `-input INPUT` Specify the input folder containing videos.
- `-output OUTPUT` Designate the output folder for PNG frames.

This tool is perfect for those who prefer the control and flexibility of the command line, offering a simple yet powerful solution for converting videos to frames on Linux systems.

---

These tools are crafted to aid in your dataset preparation and enhancement, offering a blend of simplicity and functionality. Should you have any questions or need further support, please feel free to reach out.

---
