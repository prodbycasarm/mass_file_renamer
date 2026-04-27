## 📄 Description
This script was created to batch-rename PNG files that share a common substring (e.g., `-resized`) in their filenames.

In cases where files all have different names but include a common pattern you want removed, manually renaming them can be tedious. This Python script automates the process by removing the specified substring from all matching files at once.

---

## 🖼️ Related Use Case
This script is useful when working with large batches of images that need to be resized or processed.

You can use tools like:
https://www.bulk.pics/resize

## 🚀 Usage
1. Set the **input folder path** in the script (this is where you will place the files to be renamed).
2. Set the **output folder path** (this is where the renamed files will be saved).
3. Place your files into the input folder.
4. Run the script:

```bash
python rename.py