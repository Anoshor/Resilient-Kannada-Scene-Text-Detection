import os

folder_path = "E:\cropped ds"
image_files = os.listdir(folder_path)
image_files.sort()  # This sorts the files in alphabetical order

for i, filename in enumerate(image_files, start=1):
    new_filename = f"{i:03d}.jpg"  # Change the format as needed, e.g., "{i}.jpg"
    old_path = os.path.join(folder_path, filename)
    new_path = os.path.join(folder_path, new_filename)
    os.rename(old_path, new_path)
