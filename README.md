# RenameDateTaken

This script is designed to rename `.jpg` files in a specified directory based on date taken in their EXIF data. This is useful for photographer who likes to rename all their files based on date taken for easier sorting.

## Description

The script iterates over all `.jpg` files within the given directory, reads the EXIF data to extract the original date and time the photo was taken, and renames the file accordingly. If a file cannot be renamed due to a naming conflict, the script will add one second to the original timestamp and attempt to rename it again.

## Requirements

- Python 3
- Pillow library
- exif library

## Usage

1. Install the required libraries (if not already installed):
   ```bash
   pip install Pillow exif
2. Run the script with the directory path as an argument:
   python rename_files.py <directory_path>

## License

MIT
