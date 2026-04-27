## 📄 Description
This script was created to batch-rename PNG files that share a common substring (e.g., `-resized`) in their filenames.

In cases where files all have different names but include a common pattern you want removed, manually renaming them can be tedious. This Python script automates the process by removing the specified substring from all matching files at once.

---

## 🖼️ Related Use Case
This script is useful when working with large batches of images that need to be resized or processed.

You can use tools like:
https://www.bulk.pics/resize

## 🚀 Usage

1. Run the script
```python rename.py```

2. Place your files into the input folder.
3. Set the input folder path in the script (this is where your files to be renamed are located).
4. Set the output folder path in the script (this is where the renamed files will be saved).
5. Define what you would like to remove from all files (e.g. -resized).
6. If you want all files with different names to include a common word, you can add it in the Replace With section.
7. Click Run Rename.

## 🚀 Warning

Since this tool modifies file names and performs batch file operations, your antivirus software may flag the executable version (`.exe`) as a potential threat.

This is a **false positive** that can happen when the script is packaged (e.g. using PyInstaller), because it:
- Bundles Python into a single executable
- Extracts files temporarily at runtime
- Performs bulk file operations (rename/copy)

### 🟢 Safety Note
This tool is safe to use if obtained from here.

If your antivirus warns you:
- You can add the executable in your excluded files on your antivirus
- Or run the Python script directly instead of the executable

