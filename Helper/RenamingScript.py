import os
def rename_files_in_folder(folder_path):
    files = os.listdir(folder_path)
    files.sort()
    for index, filename in enumerate(files, start=1):
        file_extension = os.path.splitext(filename)[1]
        new_filename = f"{index}{file_extension}"
        old_file_path = os.path.join(folder_path, filename)
        new_file_path = os.path.join(folder_path, new_filename)
        os.rename(old_file_path, new_file_path)
    print(f"Renamed {len(files)} files in '{folder_path}'")
folder_path = '/path/to/your/folder'
rename_files_in_folder(folder_path)
