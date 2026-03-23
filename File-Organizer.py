import os
import shutil

folder = input("Enter the folder path to organize: ")

os.makedirs(os.path.join(folder, "PDFs"), exist_ok=True)
os.makedirs(os.path.join(folder, "Images"), exist_ok=True)

files = os.listdir(folder)

for file in files:
    full_path = os.path.join(folder, file)

    if not os.path.isfile(full_path):
        continue

    if file.endswith(".pdf"):
        shutil.move(full_path, os.path.join(folder, "PDFs", file))
        print(f"Moved '{file}' → PDFs/")

    elif file.endswith(".png") or file.endswith(".jpg"):
        shutil.move(full_path, os.path.join(folder, "Images", file))
        print(f"Moved '{file}' → Images/")

print("\nDone! Files have been organized.")
