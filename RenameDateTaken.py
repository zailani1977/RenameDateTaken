"""
Script Name: RenameDateTaken.py
Author: Zailani
Version: 1.0.0
Description: 
    This Python script rename all JPG files in a folder with the date taken time stamp. 
Dependencies:
    exif
    PIL
"""
from PIL import Image
import exif
import argparse
from datetime import datetime, timedelta
import os

def changeExifDate(directory):
    # Iterate over all the JPG files in the directory
    for filename in os.listdir(directory):
        filename = filename.lower()
        if filename.endswith(".jpg"):
            # Create the full file path
            image_file = os.path.join(directory, filename)

            # Open the image file and read the exif data
            with open(image_file, 'rb') as image:
                exif_data = Image.open(image)._getexif()

            # Get the DateTimeOriginal value as a datetime object
            original_date = datetime.strptime(exif_data[36867], '%Y:%m:%d %H:%M:%S')

            # Convert the date to a string
            date_str = original_date.strftime("%d%m%y%H%M%S")

            # Rename the file
            new_filename = f"IMG_{date_str}.JPG"
            try:
                os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))
            except:
                print ("Unable to rename " + filename + " into " + new_filename)
                
                # Add 1 second to the original_date variable
                new_date = original_date + timedelta(seconds=1) 
                
                # Convert the date to a string
                date_str = new_date.strftime("%d%m%y%H%M%S")

                # Rename the file
                new_filename = f"IMG_{date_str}.JPG"
                os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))
                print ("Using the name " + new_filename)
                continue

if __name__ == '__main__':
    # Parse command-line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('directory', help='Directory containing JPG files')
    args = parser.parse_args()

    # Call the sub function to change the exif date for each JPG file in the directory
    changeExifDate(args.directory)