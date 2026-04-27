import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
import traceback
import datetime

class RenameApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Mass File Renamer (Debug Mode)")
        self.root.geometry("600x450")
        self.root.resizable(False, False)

        self.input_folder = ""
        self.output_folder = ""

        style = ttk.Style()
        style.theme_use("clam")

        style.configure("TButton", padding=8, font=("Segoe UI", 10))
        style.configure("TLabel", font=("Segoe UI", 10))
        style.configure("Header.TLabel", font=("Segoe UI", 14, "bold"))

        # Header
        ttk.Label(root, text="Mass File Renamer (Debug Mode)", style="Header.TLabel").pack(pady=10)

        frame = ttk.Frame(root, padding=15)
        frame.pack(fill="both", expand=True)

        # Buttons
        ttk.Button(frame, text="📂 Select Input Folder", command=self.select_input).pack(fill="x", pady=5)
        ttk.Button(frame, text="📁 Select Output Folder", command=self.select_output).pack(fill="x", pady=5)

        ttk.Separator(frame).pack(fill="x", pady=10)

        # Fields
        ttk.Label(frame, text="Text to remove:").pack(anchor="w")
        self.remove_entry = ttk.Entry(frame)
        self.remove_entry.pack(fill="x", pady=5)

        ttk.Label(frame, text="Replace with (optional):").pack(anchor="w")
        self.replace_entry = ttk.Entry(frame)
        self.replace_entry.pack(fill="x", pady=5)

        ttk.Separator(frame).pack(fill="x", pady=10)

        ttk.Button(frame, text="⚡ Run Rename", command=self.rename_files).pack(fill="x", pady=5)

        # Status
        self.status = ttk.Label(frame, text="Status: Waiting...", wraplength=550)
        self.status.pack(pady=10)

        # 🔥 Debug log box
        ttk.Label(frame, text="Debug log:").pack(anchor="w")

        self.log_box = tk.Text(frame, height=10, wrap="word")
        self.log_box.pack(fill="both", expand=True)

    # ---------------- DEBUG LOGGING ----------------
    def log(self, message):
        timestamp = datetime.datetime.now().strftime("%H:%M:%S")
        line = f"[{timestamp}] {message}\n"

        print(line.strip())  # also prints in terminal if visible
        self.log_box.insert(tk.END, line)
        self.log_box.see(tk.END)

    # ---------------- FOLDERS ----------------
    def select_input(self):
        self.input_folder = filedialog.askdirectory()
        self.log(f"Selected input folder: {self.input_folder}")
        self.update_status()

    def select_output(self):
        self.output_folder = filedialog.askdirectory()
        self.log(f"Selected output folder: {self.output_folder}")
        self.update_status()

    def update_status(self):
        self.status.config(
            text=f"Input: {self.input_folder or 'Not selected'}\nOutput: {self.output_folder or 'Not selected'}"
        )

    # ---------------- MAIN LOGIC ----------------
    def rename_files(self):
        try:
            if not self.input_folder or not self.output_folder:
                messagebox.showerror("Error", "Please select both folders.")
                return

            remove_text = self.remove_entry.get()
            replace_text = self.replace_entry.get()

            if not remove_text:
                messagebox.showerror("Error", "Please enter text to remove.")
                return

            self.log("Starting batch rename process...")
            self.log(f"Remove: '{remove_text}' | Replace: '{replace_text}'")

            os.makedirs(self.output_folder, exist_ok=True)

            files = os.listdir(self.input_folder)
            self.log(f"Found {len(files)} files")

            count = 0
            skipped = 0

            for filename in files:
                try:
                    if remove_text not in filename:
                        self.log(f"Skipped (no match): {filename}")
                        skipped += 1
                        continue

                    new_name = filename.replace(remove_text, replace_text)

                    src = os.path.join(self.input_folder, filename)
                    dst = os.path.join(self.output_folder, new_name)

                    shutil.copy2(src, dst)

                    self.log(f"Copied: {filename} → {new_name}")
                    count += 1

                except Exception as file_error:
                    self.log(f"ERROR processing {filename}: {file_error}")
                    self.log(traceback.format_exc())

            result_msg = f"Done ✔ {count} renamed, {skipped} skipped."
            self.log(result_msg)

            self.status.config(text=result_msg)
            messagebox.showinfo("Done", result_msg)

        except Exception as e:
            self.log("FATAL ERROR:")
            self.log(str(e))
            self.log(traceback.format_exc())
            messagebox.showerror("Fatal Error", str(e))


# Run app
root = tk.Tk()
app = RenameApp(root)
root.mainloop()