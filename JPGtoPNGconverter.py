import sys
import os
from pathlib import Path
from PIL import Image
import pdb

# Runs with respect to the current directory
if __name__ == "__main__":
    # 2 arguments are as follow <source folder> <destination folder>
    origin_folder, dest_folder = sys.argv[1], sys.argv[2]
    origin_folder = os.path.abspath(origin_folder)

    # Create <destination> folder if it does not already exist.
    if os.path.exists(dest_folder) == False:
        os.mkdir(dest_folder)
    dest_folder = os.path.abspath(dest_folder)
    # Convert all imanges inside <source> folder.
    try:
        for item in os.listdir(origin_folder):
            full_path_item = os.path.join(origin_folder, item)
            # pdb.set_trace()
            print(f'Source file: {full_path_item}')
            base, ext = os.path.splitext(item)
            outfile = os.path.join(dest_folder, base + ".png")
            print(f'PNG File: {outfile}')
            # pdb.set_trace()
            with Image.open(full_path_item) as im:
                im.save(outfile)
    except FileNotFoundError:
        print("File not found: ", origin_folder)
        print("Do you have the folder name correct?")
