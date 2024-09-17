import os
import shutil

# Define the paths
directory = '/your/input/path'  # Replace with the path to your input folder
output_folder = '/your/output/path'  # Replace with the path to your output folder

# Ensure the output folder exists, if not, create it
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for path, folders, files in os.walk(directory):
    # List contain of folder
    for folder_name in folders:
        print(f"Content of '{folder_name}'")
        # List content from folder
        print(os.listdir(f"{path}/{folder_name}"))
        folder_path = os.path.join(path, folder_name)
        folder_files = os.listdir(folder_path)
        print()

        if '0.jpg' in folder_files: #'0.jpg' to be copied
            src = os.path.join(folder_path, '0.jpg')  # Source file path
            dest = os.path.join(output_folder, f"{folder_name}_0.jpg")  # Destination file path with folder name prefix to avoid overwrite
            shutil.copyfile(src, dest)
            print(f"Copied '0.jpg' from '{folder_name}' to '{output_folder}' as '{folder_name}_0.jpg'")
        
        print()  # Blank line for better readability
    
    # Stop the loop after processing the first level (subfolders) if needed
    break