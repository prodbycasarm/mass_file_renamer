import os
import shutil

input_folder = r"C:\Users\Armado\Documents\Coding_Projects\myprojects\GTA5 tools\mass_file_rename_scipt\input"
output_folder = r"C:\Users\Armado\Documents\Coding_Projects\myprojects\GTA5 tools\mass_file_rename_scipt\output"

os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(input_folder):
    if "-resized" in filename:
        new_name = filename.replace("-resized", "")
        
        src_path = os.path.join(input_folder, filename)
        dst_path = os.path.join(output_folder, new_name)

        shutil.copy2(src_path, dst_path)
        print(f"{filename} -> {new_name}")

print("Done.")