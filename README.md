# File Type Identifier Using Magic Numbers (Cybersecurity & Malware Analysis Tool)

## 📄 One-Line Description

A modern, multithreaded GUI application that identifies real file types via binary signatures (Magic Numbers) to uncover hidden extensions, detect masqueraded malware, and mitigate phishing vectors.

## 🏷️ Tags

`#Cybersecurity` `#MalwareAnalysis` `#MagicNumbers` `#Python` `#CustomTkinter` `#DigitalForensics` `#AntiPhishing` `#DefensiveSecurity` `#BinaryAnalysis` `#SecOps`

# 📝 Project Overview & Introduction

The **File Type Identifier Using Magic Numbers** is a legitimate, lightweight defensive security and malware analysis tool.

In cybersecurity, attackers frequently disguise executable files or malicious scripts as benign documents (e.g., renaming `malware.exe` to `invoice.pdf` or `photo.jpg`). Relying purely on the operating system's file extension handler leaves users vulnerable to spoofing.

This utility addresses that vulnerability by bypassing the file extension entirely. It reads the raw binary header (the first few bytes) of a file, matches it against a comprehensive signature database (**Magic Numbers**), compares the true identity with the user-facing file extension, and immediately flags any discrepancies or potential threats.

![Screenshot 1](https://github.com/SyedShaheerHussain/File-Type-Identifier_V1_GUI_Python/blob/main/FileTypeIdentifierV1/screenshots/Screenshot%20(179).png)

![Screenshot 2](https://github.com/SyedShaheerHussain/File-Type-Identifier_V1_GUI_Python/blob/main/FileTypeIdentifierV1/screenshots/Screenshot%20(180).png)

# 🎯 Mission & Objectives

* **Eliminate Blind Trust:** Break reliance on superficial file extensions.
* **Empower Malware Analysts:** Provide triage capabilities to identify binary formats.
* **Enhance Phishing Defense:** Detect deceptive file configurations before execution.
* **Deliver Accessible Security:** Package digital forensic concepts into an intuitive, high-performance GUI.

# 🏗️ Technical Architecture & Concepts

## How It Works (The Core Concept)

Every standard file format embeds a unique sequence of bytes at its absolute beginning, known as a **Magic Number** or **File Signature**.

* Operating systems use Extensions (`.png`) for superficial association.
* Applications use Magic Numbers (`\x89PNG\r\n\x1a\n`) for data integrity.

This application forces a strict validation comparison:

```math
\text{Status} =
\begin{cases}
\text{Safe/Match} & \text{if File Extension} = \text{Detected Magic Number Signature} \\
\text{Mismatch/Threat} & \text{if File Extension} \neq \text{Detected Magic Number Signature}
\end{cases}
```

## Textual Architecture Flowchart

```text
[User Selects File / Folder]
            │
            ▼
   [Scanner Module] ───► Opens file in Raw Binary Read Mode ("rb")
            │
            ▼
   [Header Extraction] ───► Reads first 64 bytes of data
            │
            ▼
[Signature Comparison] ◄─── Matches against magic_db.py JSON-like Dictionary
            │
            ├───► Match Found? ───► Extracted True MIME/Type
            └───► No Match?    ───► Categorized as "unknown"
            │
            ▼
[Validation Engine] ───► Boolean evaluation: (Extension == True Type)
            │
            ├───► TRUE  ───► Log Status: Clear
            └───► FALSE ───► Log Status: MISMATCH (Flagged Threat)
            │
            ▼
[UI Main Thread Updates] ───► Pushes asynchronously via UI .after() hook
```

# 🔒 Phishing Defense, Email Security, & Cyber Safety

## What is Phishing & Email Spoofing?

Phishing is a social engineering attack where malicious actors trick targets into revealing sensitive credentials or downloading malicious payloads. A high-risk delivery method is email attachments where the extension is manipulated to exploit human psychology.

## How Attackers Deceive Users

### Double Extensions

Naming a file:

```text
document.pdf.exe
```

If extensions are hidden in Windows, the user only sees:

```text
document.pdf
```

### Right-to-Left Override (RLO)

Exploiting Unicode characters to flip the visual representation of text:

```text
annex_gpj.exe
```

appears visually as:

```text
annex_exe.jpg
```

### Mismatched Headers

Sending a dangerous executable or script while altering its extension to a harmless format such as:

* `.txt`
* `.png`

waiting for execution through system misconfiguration or vulnerability exploitation.

## How to Protect Yourself and Detect Breaches

1. Never open unexpected attachments.
2. Verify the sender through an out-of-band communication channel.
3. Verify suspicious files using Magic Number analysis.
4. Look for mismatches between extension and actual file type.

Example:

```text
Claims to be: photo.jpg
Actual type: exe
```

This is a strong indicator of compromise (IoC).

# 📈 Market Value & Professional Use Cases

## Security Operations Centers (SOC)

Analysts can perform initial triage on user-reported phishing attachments without exposing endpoints to execution risks.

## Incident Response (IR)

Responders can sweep directories for hidden executables deployed by threat actors maintaining persistence.

## Academic & Educational

Useful for students studying:

* Digital Forensics
* Malware Reverse Engineering
* Low-Level Computing
* Binary Analysis

# 🛠️ Technologies & Languages Used

| Component            | Technology               |
| -------------------- | ------------------------ |
| Programming Language | Python 3.10+             |
| GUI Framework        | CustomTkinter            |
| Drag-and-Drop        | TkinterDnD2              |
| Image Processing     | Pillow (PIL Fork)        |
| Concurrency          | Python Threading Library |

# 📁 Project Directory Structure

```text
FileTypeIdentifier/
│
├── main.py
├── magic_db.py
├── scanner.py
├── exports.py
├── requirements.txt
│
├── assets/
│   └── logo.png
│
└── reports/
```

# 💻 Source Code Listings

## 1. requirements.txt

```txt
customtkinter
tkinterdnd2
Pillow
```

# 🛠️ Features & Functions Detailed Breakdown

## Core Features

* ✨ Multi-Extension Check
* 🚀 Asynchronous Worker Engines
* 📊 Real-Time Threat Metrics
* 📝 JSON & TXT Report Exporting

# 📈 Advantages & Disadvantages

## Advantages

### Low Memory Footprint

Reads only:

```python
f.read(64)
```

allowing extremely fast processing of large files.

### Offline-First Protocol

No external communication required.

### Cross-Platform Compatibility

Runs on:

* Windows
* Linux
* macOS

## Disadvantages

### Shared Compound Magic Numbers

Office documents and ZIP archives share:

```text
50 4B 03 04
```

requiring deeper inspection.

### Header-Stripping Evasion

Attackers may intentionally remove or alter file signatures, resulting in:

```text
unknown
```

classification.

# 🚀 Complete Step-by-Step Deployment & Configuration Guide

## Where to Run?

This application runs entirely on:

```text
localhost
```

No internet connection, web server, or open ports are required.

## Installation

### 1. Install Python

Install:

```text
Python 3.10+
```
and ensure it is added to your system PATH.

### 2. Create Project Directory

```text
FileTypeIdentifier/
```
Place all source files inside this folder.

### 3. Install Dependencies

```bash
pip install customtkinter tkinterdnd2 Pillow
```
## Running the Application

```bash
python main.py
```
## How to Use

### Scan a Single File

1. Click **Scan File**
2. Select a file
3. Check the **Mismatch** column

```text
YES = Potential Threat
NO  = Match Verified
```

### Scan an Entire Folder

1. Click **Scan Folder**
2. Select a directory
3. Review all results

### Export Reports

* Export JSON
* Export TXT

Reports are saved directly to disk.

# ⚠️ Key Notes, Cautions, & Disclaimer

## Disclaimer

This software is provided **"as is"** for educational, forensic triage, and security awareness purposes.

It is **not a replacement** for:

* Endpoint Detection & Response (EDR)
* Malware Sandboxes
* Antivirus Platforms
* Threat Hunting Suites

A successful scan does **not** guarantee a file is malware-free.

# 🧠 Lessons Learned & Concepts Studied

* Byte-level file analysis using binary streams
* Multithreaded GUI architecture
* File spoofing and social engineering attack techniques
* Magic Number signature validation
* Event-driven interface design

# 🔮 Future Enhancements & Implementations

## Entropy Analysis Mapping

Detect packed, compressed, or encrypted malware payloads.

## Deep XML Inspection Engine

Differentiate:

* `.docx`
* `.xlsx`
* `.pptx`
* `.zip`

through internal archive inspection.

## YARA Rule Integration

Combine file signature validation with advanced pattern-based malware detection.

# ⚖️ Copyright & Author Information

**Developed By:** Syed Shaheer Hussain

**Copyright Horizon:** © 2026 Syed Shaheer Hussain. All Rights Reserved.

**Licensing Agreement:** Licensed strictly for security awareness, local administrative triage, and instructional computing models. Use responsibly to secure your environments.
