import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk

class RenameApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Mass File Renamer")
        self.root.geometry("520x380")
        self.root.resizable(False, False)

        self.input_folder = ""
        self.output_folder = ""

        style = ttk.Style()
        style.theme_use("clam")

        style.configure("TButton", padding=8, font=("Segoe UI", 10))
        style.configure("TLabel", font=("Segoe UI", 10))
        style.configure("Header.TLabel", font=("Segoe UI", 14, "bold"))

        # Header
        ttk.Label(root, text="Mass File Renamer", style="Header.TLabel").pack(pady=10)

        frame = ttk.Frame(root, padding=15)
        frame.pack(fill="both", expand=True)

        # Folder buttons
        ttk.Button(frame, text="📂 Select Input Folder", command=self.select_input).pack(fill="x", pady=5)
        ttk.Button(frame, text="📁 Select Output Folder", command=self.select_output).pack(fill="x", pady=5)

        ttk.Separator(frame).pack(fill="x", pady=10)

        # Remove field
        ttk.Label(frame, text="Text to remove:").pack(anchor="w")
        self.remove_entry = ttk.Entry(frame)
        self.remove_entry.pack(fill="x", pady=5)

        # Replace field
        ttk.Label(frame, text="Replace with (optional):").pack(anchor="w")
        self.replace_entry = ttk.Entry(frame)
        self.replace_entry.pack(fill="x", pady=5)

        ttk.Separator(frame).pack(fill="x", pady=10)

        # Run button
        ttk.Button(frame, text="⚡ Run Rename", command=self.rename_files).pack(fill="x", pady=5)

        # Status
        self.status = ttk.Label(frame, text="Status: Waiting...", wraplength=450)
        self.status.pack(pady=15)

    def select_input(self):
        self.input_folder = filedialog.askdirectory()
        self.update_status()

    def select_output(self):
        self.output_folder = filedialog.askdirectory()
        self.update_status()

    def update_status(self):
        self.status.config(
            text=f"Input: {self.input_folder or 'Not selected'}\nOutput: {self.output_folder or 'Not selected'}"
        )

    def rename_files(self):
        if not self.input_folder or not self.output_folder:
            messagebox.showerror("Error", "Please select both folders.")
            return

        remove_text = self.remove_entry.get()
        replace_text = self.replace_entry.get()

        if remove_text == "":
            messagebox.showerror("Error", "Please enter text to remove.")
            return

        os.makedirs(self.output_folder, exist_ok=True)

        count = 0

        for filename in os.listdir(self.input_folder):
            if remove_text in filename:
                new_name = filename.replace(remove_text, replace_text)

                src = os.path.join(self.input_folder, filename)
                dst = os.path.join(self.output_folder, new_name)

                shutil.copy2(src, dst)
                count += 1

        messagebox.showinfo("Done", f"Processed {count} files.")
        self.status.config(text=f"Done ✔ {count} files renamed.")

# Run app
root = tk.Tk()
app = RenameApp(root)
root.mainloop()