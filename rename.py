import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox
import traceback
import datetime


class RenameApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Mass File Renamer")
        self.root.geometry("560x650")
        self.root.resizable(False, False)
        self.root.configure(bg="#0f1115")
        self.input_folder = ""
        self.output_folder = ""
        self.input_label = None
        self.output_label = None
        self.input_open_btn = None
        self.output_open_btn = None

        # ---------------- COLORS ----------------
        self.bg = "#0f1115"
        self.card = "#161a22"
        self.text = "#e6e6e6"
        self.muted = "#9aa4b2"
        self.accent = "#3b82f6"
        self.danger = "#ef4444"

        # ---------------- HEADER ----------------
        header = tk.Label(
            root,
            text="Mass File Renamer",
            bg=self.bg,
            fg=self.text,
            font=("Segoe UI", 18, "bold")
        )
        header.pack(pady=12)

        # ---------------- MAIN FRAME ----------------
        frame = tk.Frame(root, bg=self.bg)
        frame.pack(fill="both", expand=True, padx=15)

        # ---------------- INPUT ROW ----------------
        tk.Label(frame, text="Input Folder", bg=self.bg, fg=self.muted).pack(anchor="w")

        input_row = tk.Frame(frame, bg=self.bg)
        input_row.pack(fill="x", pady=3)

        tk.Button(
            input_row,
            text="📂 Select Input",
            command=self.select_input,
            bg="#262b36",
            fg=self.text,
            relief="flat"
        ).pack(side="left", expand=True, fill="x", padx=(0, 5))

        self.input_open_btn = tk.Button(
            input_row,
            text="Open",
            command=self.open_input_folder,
            bg="#1f2937",
            fg=self.text,
            relief="flat",
            state="disabled"
        )
        self.input_open_btn.pack(side="right")

        self.input_label = tk.Label(frame, text="Not selected", bg=self.bg, fg=self.danger)
        self.input_label.pack(anchor="w", pady=(0, 8))


        # ---------------- OUTPUT ROW ----------------
        tk.Label(frame, text="Output Folder", bg=self.bg, fg=self.muted).pack(anchor="w")

        output_row = tk.Frame(frame, bg=self.bg)
        output_row.pack(fill="x", pady=3)

        tk.Button(
            output_row,
            text="📁 Select Output",
            command=self.select_output,
            bg="#262b36",
            fg=self.text,
            relief="flat"
        ).pack(side="left", expand=True, fill="x", padx=(0, 5))

        self.output_open_btn = tk.Button(
            output_row,
            text="Open",
            command=self.open_output_folder,
            bg="#1f2937",
            fg=self.text,
            relief="flat",
            state="disabled"
        )
        self.output_open_btn.pack(side="right")

        self.output_label = tk.Label(frame, text="Not selected", bg=self.bg, fg=self.danger)
        self.output_label.pack(anchor="w", pady=(0, 8))

        # ---------------- CARD: OPTIONS ----------------
        self.section_title(frame, "Rename Options")

        tk.Label(frame, text="Text to remove", bg=self.bg, fg=self.muted).pack(anchor="w")
        self.remove_entry = self.entry(frame)

        tk.Label(frame, text="Replace with (optional)", bg=self.bg, fg=self.muted).pack(anchor="w", pady=(8, 0))
        self.replace_entry = self.entry(frame)

        # ---------------- RUN BUTTON ----------------
        self.btn("⚡ Run Rename", self.rename_files, frame, primary=True)

        # ---------------- STATUS ----------------
        self.status = tk.Label(
            frame,
            text="Ready",
            bg=self.bg,
            fg=self.muted,
            font=("Segoe UI", 9)
        )
        # Do NOT pack it here. It stays hidden until check_status() is called.

        # ---------------- LOG ----------------
        tk.Label(frame, text="Debug Log", bg=self.bg, fg=self.text, font=("Segoe UI", 10, "bold")).pack(anchor="w")

        self.log_box = tk.Text(
            frame,
            height=10,
            bg="#0b0d12",
            fg="#cbd5e1",
            insertbackground="white",
            relief="flat"
        )
        self.log_box.pack(fill="both", expand=True, pady=5)

    # ---------------- UI HELPERS ----------------
    def section_title(self, parent, text):
        tk.Label(parent, text=text, bg=self.bg, fg=self.text, font=("Segoe UI", 12, "bold")).pack(anchor="w", pady=(10, 5))

    def entry(self, parent):
        e = tk.Entry(parent, bg="#1c2230", fg=self.text, insertbackground="white",
                     relief="flat", font=("Segoe UI", 10))
        e.pack(fill="x", pady=4)
        return e

    def btn(self, text, cmd, parent, primary=False, secondary=False):
        if primary:
            bg = self.accent
            fg = "white"
        elif secondary:
            bg = "#1f2937"
            fg = self.text
        else:
            bg = "#262b36"
            fg = self.text

        b = tk.Button(
            parent,
            text=text,
            command=cmd,
            bg=bg,
            fg=fg,
            activebackground="#374151",
            activeforeground="white",
            relief="flat",
            pady=8,
            font=("Segoe UI", 10)
        )
        b.pack(fill="x", pady=4)

    # ---------------- LOGGING ----------------
    def log(self, message):
        time = datetime.datetime.now().strftime("%H:%M:%S")
        line = f"[{time}] {message}\n"
        print(line.strip())
        self.log_box.insert(tk.END, line)
        self.log_box.see(tk.END)

    # ---------------- FOLDERS ----------------

    def select_input(self):
        folder = filedialog.askdirectory()
        if folder:
            self.input_folder = folder
            self.input_label.config(text=folder, fg=self.accent)
            self.input_open_btn.config(state="normal")
            self.log(f"Input set to: {folder}")

    def select_output(self):
        folder = filedialog.askdirectory()
        if folder:
            self.output_folder = folder
            self.output_label.config(text=folder, fg=self.accent)
            self.output_open_btn.config(state="normal")
            self.log(f"Output set to: {folder}")

    def open_input_folder(self):
        if not self.input_folder:
            messagebox.showwarning("Warning", "Input folder not selected.")
            return

        if os.path.exists(self.input_folder):
            self.log(f"Opening input folder: {self.input_folder}")
            os.startfile(self.input_folder)
        else:
            messagebox.showerror("Error", "Input folder does not exist.")


    def open_output_folder(self):
        if not self.output_folder:
            messagebox.showwarning("Warning", "Output folder not selected.")
            return

        if os.path.exists(self.output_folder):
            self.log(f"Opening output folder: {self.output_folder}")
            os.startfile(self.output_folder)
        else:
            messagebox.showerror("Error", "Output folder does not exist.")
            



    def select_input(self):
        folder = filedialog.askdirectory()
        if folder:
            self.input_folder = folder
            self.input_label.config(text=folder, fg=self.accent)
            self.input_open_btn.config(state="normal")
            self.log(f"Input set to: {folder}")
            self.check_status()  # Added this

    def select_output(self):
        folder = filedialog.askdirectory()
        if folder:
            self.output_folder = folder
            self.output_label.config(text=folder, fg=self.accent)
            self.output_open_btn.config(state="normal")
            self.log(f"Output set to: {folder}")
            self.check_status()  # Added this

    def check_status(self):
        """Shows the status label only when both folders are ready"""
        if self.input_folder and self.output_folder:
            self.status.pack(pady=5, before=self.log_box.master.winfo_children()[-2]) 
            self.status.config(text="Ready")
    # ---------------- MAIN LOGIC ----------------
    def rename_files(self):
        try:
            if not self.input_folder or not self.output_folder:
                messagebox.showerror("Error", "Select both folders.")
                return

            remove_text = self.remove_entry.get()
            replace_text = self.replace_entry.get()

            if not remove_text:
                messagebox.showerror("Error", "Enter text to remove.")
                return

            self.log("Starting rename process...")

            os.makedirs(self.output_folder, exist_ok=True)

            files = os.listdir(self.input_folder)

            count = 0
            skipped = 0

            for f in files:
                if remove_text not in f:
                    skipped += 1
                    continue

                new_name = f.replace(remove_text, replace_text)

                src = os.path.join(self.input_folder, f)
                dst = os.path.join(self.output_folder, new_name)

                shutil.copy2(src, dst)

                self.log(f"{f} → {new_name}")
                count += 1

            msg = f"Done ! {count} renamed, {skipped} skipped"
            self.status.config(text=msg)
            self.log(msg)
            messagebox.showinfo("Done", msg)

        except Exception as e:
            self.log("ERROR")
            self.log(str(e))
            self.log(traceback.format_exc())


# ---------------- RUN ----------------
root = tk.Tk()
app = RenameApp(root)
root.mainloop()