import os
import shutil

input_folder = r"folder_location\input"
output_folder = r"folder_location\output"

os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(input_folder):
    if "-resized" in filename:
        new_name = filename.replace("-resized", "")
        
        src_path = os.path.join(input_folder, filename)
        dst_path = os.path.join(output_folder, new_name)

        shutil.copy2(src_path, dst_path)
        print(f"{filename} -> {new_name}")

print("Done.")