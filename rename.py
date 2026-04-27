import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

class RenameApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Mass File Renamer")
        self.root.geometry("500x300")

        self.input_folder = ""
        self.output_folder = ""

        # UI Elements
        tk.Button(root, text="Select Input Folder", command=self.select_input).pack(pady=10)
        tk.Button(root, text="Select Output Folder", command=self.select_output).pack(pady=10)
        tk.Button(root, text="Run Rename", command=self.rename_files, bg="green", fg="white").pack(pady=10)

        self.status = tk.Label(root, text="Status: Waiting...", wraplength=450)
        self.status.pack(pady=20)

    def select_input(self):
        self.input_folder = filedialog.askdirectory()
        self.status.config(text=f"Input: {self.input_folder}")

    def select_output(self):
        self.output_folder = filedialog.askdirectory()
        self.status.config(text=f"Output: {self.output_folder}")

    def rename_files(self):
        if not self.input_folder or not self.output_folder:
            messagebox.showerror("Error", "Please select both folders")
            return

        os.makedirs(self.output_folder, exist_ok=True)

        count = 0

        for filename in os.listdir(self.input_folder):
            if "-resized" in filename:
                new_name = filename.replace("-resized", "")

                src = os.path.join(self.input_folder, filename)
                dst = os.path.join(self.output_folder, new_name)

                shutil.copy2(src, dst)
                count += 1

        self.status.config(text=f"Done! Renamed {count} files.")
        messagebox.showinfo("Complete", f"Finished renaming {count} files.")

# Run app
root = tk.Tk()
app = RenameApp(root)
root.mainloop()