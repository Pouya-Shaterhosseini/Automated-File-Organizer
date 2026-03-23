# Automated-File-Organizer
A Python utility script that automates the organization of cluttered folders. It scans a directory and sorts files into specific subfolders based on their file extensions.

## Features
- **Automatic Directory Creation:** Automatically creates `PDFs` and `Images` folders if they don't exist.
- **File Sorting:** Moves `.pdf` files to the PDFs folder and `.png`/`.jpg` files to the Images folder.
- **Smart Filtering:** Distinguishes between files and subfolders to prevent errors during the moving process.

## Technologies Used
- **Language:** Python 3.x
- **Libraries:** `os`, `shutil` (Standard Libraries)

## How to Use
1. Run the script.
2. Enter the full path of the folder you wish to organize when prompted.
3. The script will display a log of all moved files.
