import os

folder_path = "C:\\Users\\anosh\\OneDrive\\Desktop\\research\\codes\\internship\\picsano"

all_files = os.listdir(folder_path)

# for file in all_files:
#     if file.endswith('.txt') or file.endswith('.jpg'):
#         new_name = file.replace("res_", "")
#         old_path = os.path.join(folder_path, file)
#         new_path = os.path.join(folder_path, new_name)
#         os.rename(old_path, new_path)

for file in all_files:
    if file.endswith('_mask.jpg'):
        file_path = os.path.join(folder_path, file)
        os.remove(file_path)