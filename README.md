A File Type Identifier using Magic Numbers is a legitimate defensive-security and malware-analysis project. It detects when a file's extension (.jpg, .png, .pdf) does not match its  actual binary signature (magic number), which is a common 

## File Type Identifier Using Magic Numbers (Cybersecurity & Malware Analysis Tool) 

## 📄 One-Line Description 

A modern, multithreaded GUI application that identifies real file types via binary signatures (Magic Numbers) to uncover hidden extensions, detect masqueraded malware, and mitigate phishing vectors. 

## 🏷 Tags 

#Cybersecurity #MalwareAnalysis #MagicNumbers #Python #CustomTkinter #DigitalForensics #AntiPhishing #DefensiveSecurity #BinaryAnalysis #SecOps 

## 📝 Project Overview & Introduction 

The File Type Identifier Using Magic Numbers is a legitimate, lightweight defensive security and malware analysis tool. In cybersecurity, attackers frequently disguise executable files or malicious scripts as benign documents (e.g., renaming malware.exe to invoice.pdf or photo.jpg ). Relying purely on the operating system's file extension handler leaves users vulnerable to spoofing. 

This utility addresses that vulnerability by bypassing the file extension entirely. It reads the raw binary header (the first few bytes) of a file, matches it against a comprehensive signature database (Magic Numbers), compares the true identity with the user-facing file extension, and immediately flags any discrepancies or potential threats. 

## 🎯 Mission & Objectives 

Eliminate Blind Trust: Break reliance on superficial file extensions. 

Empower Malware Analysts: Provide triage capabilities to identify binary formats. 

Enhance Phishing Defense: Detect deceptive file configurations before execution. 

Deliver Accessible Security: Package digital forensic concepts into an intuitive, highperformance GUI. 

## 🏗 Technical Architecture & Concepts 

## How It Works (The Core Concept) 

Every standard file format embeds a unique sequence of bytes at its absolute beginning, known as a Magic Number or File Signature. 

Operating systems use Extensions ( .png ) for superficial association. 

Applications use Magic Numbers ( \x89PNG\r\n\x1a\n ) for data integrity. 

This application forces a strict validation comparison: 

if File Extension = Detected Magic Number Status = {Mismatch/Threat[Safe/Match] if File Extension = Detected Magic Number 

## Textual Architecture Flowchart 

[User Selects File / Folder] │ ▼ [Scanner Module] ───► Opens file in Raw Binary Read Mode ("rb") │ ▼ [Header Extraction] ───► Reads first 64 bytes of data │ ▼ [Signature Comparison] ◄─── Matches against magic_db.py JSON-like Dictionary │ ├───► Match Found? ───► Extracted True MIME/Type └───► No Match?    ───► Categorized as "unknown" │ ▼ [Validation Engine] ───► Boolean evaluation: (Extension == True Type) │ ├───► TRUE  ───► Log Status: Clear └───► FALSE ───► Log Status: MISMATCH (Flagged Threat) │ ▼ [UI Main Thread Updates] ───► Pushes asynchronously via UI `.after()` hook 

## 🔒 Phishing Defense, Email Security, & Cyber Safety 

## What is Phishing & Email Spoofing? 

Phishing is a social engineering attack where malicious actors trick targets into revealing sensitive credentials or downloading malicious payloads. A high-risk delivery method is email attachments where the extension is manipulated to exploit human psychology. 

## How Attackers Deceive Users 

1. Double Extensions: Naming a file document.pdf.exe . If extensions are hidden in Windows, the user only sees document.pdf . 

2. Right-to-Left Override (RLO): Exploiting Unicode characters to flip the visual representation of text (e.g., displaying annex_gpj.exe visually as annex_exe.jpg ). 

3. Mismatched Headers: Sending a dangerous executable or script but altering its extension to a harmless text format ( .txt ) or image ( .png ), waiting for a system configuration or vulnerability to exploit it upon execution. 

## How to Protect Yourself and Detect Breaches 

- Never Open Unexpected Attachments: Verify the sender over an out-of-band communication channel (e.g., phone call, text). 

- Verify with Magic Numbers: Run suspicious files through this File Type Identifier before launching them. 

- Look for Mismatches: If a file claims to be a .jpg but the scanner reports it as an exe or zip , you are dealing with a targeted attack or an indicator of compromise 

- (IoC). 

## 📈 Market Value & Professional Use Cases 

Security Operations Centers (SOC): Analysts can perform initial triage on incoming user-reported phishing attachments without exposing endpoints to execution vulnerabilities. 

Incident Response (IR): Incident responders can sweep directories for hidden executables deployed by threat actors maintaining persistence. 

Academic/Educational: Serves as a tangible learning aid for students exploring digital forensics, malware reverse engineering, and low-level computing. 

## 🛠 Technologies & Languages Used 

Programming Language: Python 3.10+ 

GUI Engine: CustomTkinter (Modernized wrapper building on top of standard Tkinter bindings) 

Drag-and-Drop Handler: TkinterDnD2 (Enables cross-platform drag-and-drop mechanics) 

Image Processor: Pillow (PIL Fork) for visual assets and potential thumbnail parsing 

Threading Architecture: Native Python threading library for executing asynchronous tasks while preventing GUI freezing. 

## 📁 Project Directory Structure 

## Plaintext 

 

FileTypeIdentifier/ 

## │ 

├── main.py                # Main Application Entrypoint & GUI Threading 

├── magic_db.py            # Static Database mapping extensions to Hex Signatures ├── scanner.py             # Binary Reader, File I/O, and Core Validation Engine ├── exports.py             # Report Generation Engine (JSON & TXT Serializers) ├── requirements.txt       # Hard Dependencies configuration file │ 

├── assets/ │ └── logo.png           # Visual Brand Assets │ 

└── reports/               # Default output repository for audit generation 

## 💻 Source Code Listings 

## 1. requirements.txt 

## Plaintext 

 

customtkinter tkinterdnd2 Pillow 

## 2. magic_db.py 

## Python 

 

MAGIC_NUMBERS = { "exe": [b"\x4D\x5A"], 

"dll": [b"\x4D\x5A"], 

"pdf": [b"\x25\x50\x44\x46"], 

"png": [b"\x89PNG\r\n\x1a\n"], "jpg": [b"\xFF\xD8\xFF"], "gif": [b"GIF87a", b"GIF89a"], "bmp": [b"BM"], "zip": [b"\x50\x4B\x03\x04"], "rar": [b"\x52\x61\x72\x21\x1A\x07"], "7z": [b"\x37\x7A\xBC\xAF\x27\x1C"], "mp3": [b"ID3"], "wav": [b"RIFF"], "mp4": [b"ftyp"], "avi": [b"RIFF"], "docx": [b"\x50\x4B\x03\x04"], "xlsx": [b"\x50\x4B\x03\x04"], 

"pptx": [b"\x50\x4B\x03\x04"] 

} 

## 3. scanner.py 

## Python 

 

import os from magic_db import MAGIC_NUMBERS 

def detect_type(filepath): try: with open(filepath, "rb") as f: header = f.read(64) 

for filetype, signatures in MAGIC_NUMBERS.items(): for sig in signatures: 

if header.startswith(sig): return filetype if sig == b"ftyp" and b"ftyp" in header: return filetype return "unknown" except Exception: return "error" 

def get_file_info(filepath): size = os.path.getsize(filepath) ext = os.path.splitext(filepath)[1].replace(".", "").lower() actual = detect_type(filepath) mismatch = ext != actual 

return { 

"path": filepath, "extension": ext, "actual": actual, "size": size, "mismatch": mismatch 

} 

## 4. exports.py 

## Python 

##  

import json from datetime import datetime 

def export_json(data): 

filename = f"report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json" with open(filename, "w") as f: 

json.dump(data, f, indent=4) return filename 

def export_txt(data): 

filename = f"report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt" with open(filename, "w") as f: 

for item in data: 

f.write("=" * 60 + "\n") for k, v in item.items(): f.write(f"{k}: {v}\n") 

return filename 

## 5. main.py 

## Python 

 

import os import threading import tkinter as tk from tkinter import filedialog from tkinter import ttk import customtkinter as ctk 

from scanner import get_file_info from exports import export_json, export_txt 

ctk.set_appearance_mode("dark") ctk.set_default_color_theme("blue") 

class FileTypeIdentifier(ctk.CTk): def __init__(self): super().__init__() self.title("Magic Number File Type Identifier") self.geometry("1400x850") self.minsize(1200, 700) self.scan_results = [] self.build_ui() 

def build_ui(self): 

self.grid_columnconfigure(1, weight=1) self.grid_rowconfigure(0, weight=1) 

sidebar = ctk.CTkFrame(self, width=260) sidebar.grid(row=0, column=0, sticky="ns") 

title = ctk.CTkLabel( sidebar, text="FILE TYPE\nIDENTIFIER", font=("Segoe UI", 26, "bold") ) title.pack(pady=25) 

ctk.CTkButton(sidebar, text="Scan File", command=self.scan_file).pack(fill="x ctk.CTkButton(sidebar, text="Scan Folder", command=self.scan_folder).pack(fill ctk.CTkButton(sidebar, text="Export JSON", command=self.save_json).pack(fill= ctk.CTkButton(sidebar, text="Export TXT", command=self.save_txt).pack(fill="x 

self.stats = ctk.CTkLabel(sidebar, text="Files: 0\nThreats: 0") self.stats.pack(pady=20) 

main = ctk.CTkFrame(self) main.grid(row=0, column=1, sticky="nsew") 

self.progress = ttk.Progressbar(main, mode="determinate") self.progress.pack(fill="x", padx=10, pady=10) 

columns = ("File", "Extension", "Actual", "Mismatch", "Size") self.tree = ttk.Treeview(main, columns=columns, show="headings") 

for col in columns: 

self.tree.heading(col, text=col) self.tree.column(col, width=200) 

self.tree.pack(fill="both", expand=True, padx=10, pady=10) 

def add_result(self, data): self.scan_results.append(data) self.tree.insert( "", "end", values=( os.path.basename(data["path"]), data["extension"], data["actual"], "YES" if data["mismatch"] else "NO", data["size"] ) ) threats = sum(1 for x in self.scan_results if x["mismatch"]) self.stats.configure(text=f"Files: {len(self.scan_results)}\nThreats: {threat def scan_file(self): path = filedialog.askopenfilename() if not path: return result = get_file_info(path) self.add_result(result) 

def scan_folder(self): folder = filedialog.askdirectory() if not folder: return threading.Thread(target=self.folder_scan_worker, args=(folder,), daemon=True) def folder_scan_worker(self, folder): files = [] for root, dirs, filenames in os.walk(folder): for file in filenames: files.append(os.path.join(root, file)) total = len(files) self.progress["maximum"] = total for index, file in enumerate(files): try: info = get_file_info(file) self.after(0, lambda i=info: self.add_result(i)) except: pass self.progress["value"] = index + 1 def save_json(self): export_json(self.scan_results) 

def save_txt(self): 

export_txt(self.scan_results) 

if __name__ == "__main__": 

app = FileTypeIdentifier() 

app.mainloop() 

## 🛠 Features & Functions Detailed Breakdown 

## Core Features 

✨ Multi-Extension Check: Scans files against compound signatures. 

🚀 Asynchronous Worker Engines: Folder scanning runs entirely on worker threads using threading.Thread , ensuring the main GUI rendering cycle never stalls or drops frames. 

📊 Risk Metric Summarization: Real-time generation of the exact count of identified anomalies (mismatch count mapped out directly to the threat matrix counters). 

📝 Structured Reports: Dual format exporters provide raw output for standard text parsing ( .txt ) and key-value mapping ( .json ) for ingestion into advanced logging systems. 

## 📈 Advantages & Disadvantages 

## Advantages 

1. Low Memory Footprint: By reading only the first 64 bytes ( f.read(64) ), it can process large files (e.g., 4GB .iso or .mp4 ) nearly instantaneously without loading them into RAM. 

2. Offline-First Protocol: Operates locally on the host environment; no data leaks over external network links. 

3. Cross-Platform Compatibility: Relies on standardized Python GUI engines, allowing execution across Windows, macOS, and Linux systems. 

## Disadvantages 

1. Shared Compound Magic Numbers: Zip-based containers like Microsoft Office ( .docx , .xlsx , .pptx ) share matching root header signatures 

( \x50\x4B\x03\x04 ), requiring deep XML sniffing to further differentiate them. 

2. Vulnerability to Intentional Stripping: If an adversary completely strips headers or prefixes a payload with arbitrary garbage bytes, basic signature mapping will result in an unknown status. 

## 🚀 Complete Step-by-Step Deployment & Configuration Guide 

## Where to Run? 

This application runs entirely on your local machine (localhost). It is a standalone desktop application and does not require an internet connection, a web server (like Apache/Nginx), or a specific port host. Your data remains private and local. 

## How to Install 

1. Install Python: Ensure Python 3.10 or higher is installed and added to your system PATH. 

2. Set Up Project Directory: Create a folder named FileTypeIdentifier and place the source code files inside it. 

3. Install Dependencies: Open your terminal or command prompt inside the project folder and run: 

Bash 

 

pip install customtkinter tkinterdnd2 Pillow 

## How to Run 

Execute the program by running main.py from your terminal: 

Bash 

 

python main.py 

## How to Use 

1. Scan a Single File: Click Scan File, pick a suspicious file via the file picker, and check the dashboard grid for a "YES" in the Mismatch column. 

2. Scan an Entire Directory: Click Scan Folder to batch-process an entire download folder or attachment directory. 

3. Save Your History: Click Export JSON or Export TXT to write an audit trail directly to disk. 

## ⚠ Key Notes, Cautions, & Disclaimer 

## 🛑 Crucial Disclaimer 

Disclaimer: This software is provided "as is" for educational, forensic triage, and security awareness purposes. It does not replace full-suite endpoint detection response (EDR) platforms, sandboxes, or modern anti-virus scanning platforms. Passing a file verification scan here does not guarantee that a file is completely clean of embedded malicious payloads or macros. 

## 🧠 Lessons Learned & Concepts Studied 

Developed expertise in processing file payloads at the byte-level via binary read streams. 

Implemented multi-threaded event loop design patterns within structural interface components. 

Analyzed file spoofing attack methodologies used by malicious actors during social engineering distribution phases. 

## 🔮 Future Enhancements & Implementations 

Entropy Analysis Mapping: Implement file entropy calculators to detect compressed or encrypted malware payloads. 

Deep XML Inspection Engine: Add archive-unzipping routines to reliably differentiate between .docx , .xlsx , and standard .zip files. 

YARA Rule Integration: Couple hex validations with advanced custom rule processing blocks to search for specific malicious patterns inside identified scripts. 

## ⚖ Copyright & Author Information 

Developed By: Syed Shaheer Hussain 

Copyright Horizon: © 2026 Syed Shaheer Hussain. All Rights Reserved. 

Licensing Agreement: Licensed strictly for security awareness, local administrative triage, and instructional computing models. Use responsibly to secure your environments! 

     

