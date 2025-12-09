# 📂 File Organizer Script

This Python script helps you **organize files by extension** into a structured folder system.  
It creates a parent folder (specified by the user) and automatically sorts files from the chosen directory into subfolders based on their file type.

---

## ✨ Features
- Cleans the terminal screen for a fresh start.
- Allows the user to:
  - Specify a parent folder name.
  - Choose whether to change the working directory.
- Creates the parent folder if it doesn’t exist.
- Iterates through all files in the directory and:
  - Skips system files (`.lnk`, `.exe`, `.ini`, `.sys`).
  - Creates subfolders for each file extension.
  - Moves files into their respective extension-based folders.

---

## 🛠️ Requirements
- Python 3.6+
- Standard libraries (`os`, `pathlib`, `datetime`) — no external dependencies.

---

## 🚀 Usage
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/file-organizer.git
   cd file-organizer
Run the script:

bash
python file_organizer.py
Follow the prompts:

Enter the name of the parent folder where files will be organized.

Decide whether to change the working directory.

The script will then create subfolders by file extension and move files accordingly.

📂 Example
Suppose your directory contains:

  ```
    report.docx
    image.png
    notes.txt
    setup.exe
  ```

After running the script with parent folder name OrganizedFiles, the structure will look like:

```
OrganizedFiles/
├── docx/
│   └── report.docx
├── png/
│   └── image.png
├── txt/
│   └── notes.txt
(setup.exe is skipped because .exe is a system file)
```

⚠️ Notes
System files (.lnk, .exe, .ini, .sys) are ignored for safety.

If the parent folder or extension subfolder already exists, the script will not recreate it.

Files are moved, not copied — they will no longer exist in the original location.

📜 License
This project is licensed under the MIT License. Feel free to use and modify it.

👨‍💻 Author
Developed by Paulo de Tarso. Contributions are welcome!
