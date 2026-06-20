import os
import threading
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk

import customtkinter as ctk

from scanner import get_file_info
from exports import export_json, export_txt

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class FileTypeIdentifier(ctk.CTk):

    def __init__(self):

        super().__init__()

        self.title("Magic Number File Type Identifier")

        self.geometry("1400x850")

        self.minsize(1200, 700)

        self.scan_results = []

        self.build_ui()

    def build_ui(self):

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        sidebar = ctk.CTkFrame(self, width=260)

        sidebar.grid(row=0, column=0, sticky="ns")

        title = ctk.CTkLabel(
            sidebar,
            text="FILE TYPE\nIDENTIFIER",
            font=("Segoe UI", 26, "bold")
        )

        title.pack(pady=25)

        ctk.CTkButton(
            sidebar,
            text="Scan File",
            command=self.scan_file
        ).pack(fill="x", padx=15, pady=8)

        ctk.CTkButton(
            sidebar,
            text="Scan Folder",
            command=self.scan_folder
        ).pack(fill="x", padx=15, pady=8)

        ctk.CTkButton(
            sidebar,
            text="Export JSON",
            command=self.save_json
        ).pack(fill="x", padx=15, pady=8)

        ctk.CTkButton(
            sidebar,
            text="Export TXT",
            command=self.save_txt
        ).pack(fill="x", padx=15, pady=8)

        self.stats = ctk.CTkLabel(
            sidebar,
            text="Files: 0\nThreats: 0"
        )

        self.stats.pack(pady=20)

        main = ctk.CTkFrame(self)

        main.grid(row=0, column=1, sticky="nsew")

        self.progress = ttk.Progressbar(
            main,
            mode="determinate"
        )

        self.progress.pack(fill="x", padx=10, pady=10)

        columns = (
            "File",
            "Extension",
            "Actual",
            "Mismatch",
            "Size"
        )

        self.tree = ttk.Treeview(
            main,
            columns=columns,
            show="headings"
        )

        for col in columns:

            self.tree.heading(col, text=col)

            self.tree.column(col, width=200)

        self.tree.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )

    def add_result(self, data):

        self.scan_results.append(data)

        self.tree.insert(
            "",
            "end",
            values=(
                os.path.basename(data["path"]),
                data["extension"],
                data["actual"],
                "YES" if data["mismatch"] else "NO",
                data["size"]
            )
        )

        threats = sum(
            1 for x in self.scan_results
            if x["mismatch"]
        )

        self.stats.configure(
            text=f"Files: {len(self.scan_results)}\nThreats: {threats}"
        )

    def scan_file(self):

        path = filedialog.askopenfilename()

        if not path:
            return

        result = get_file_info(path)

        self.add_result(result)

    def scan_folder(self):

        folder = filedialog.askdirectory()

        if not folder:
            return

        threading.Thread(
            target=self.folder_scan_worker,
            args=(folder,),
            daemon=True
        ).start()

    def folder_scan_worker(self, folder):

        files = []

        for root, dirs, filenames in os.walk(folder):

            for file in filenames:
                files.append(
                    os.path.join(root, file)
                )

        total = len(files)

        self.progress["maximum"] = total

        for index, file in enumerate(files):

            try:

                info = get_file_info(file)

                self.after(
                    0,
                    lambda i=info:
                    self.add_result(i)
                )

            except:
                pass

            self.progress["value"] = index + 1

    def save_json(self):

        export_json(self.scan_results)

    def save_txt(self):

        export_txt(self.scan_results)


if __name__ == "__main__":

    app = FileTypeIdentifier()

    app.mainloop()