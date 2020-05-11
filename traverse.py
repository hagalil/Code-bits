# A program to traverse a library recursively
import os
from pathlib import Path
def traverse_dir (dir_path, files_dict):
    items = os.listdir(dir_path)
    for item in items:
        if os.path.isdir(dir_path/item):
            files_dict[item] = "Directory"
            traverse_dir(dir_path/item, files_dict)
        else:
            files_dict[item] = "File"
    return  files_dict

dir_name = Path(input("Please enter directory path: "))
files_dict = traverse_dir(dir_name, {})
# Print names of items in directory and their type
for i in files_dict:
    print(i,"is a ", files_dict [i])
