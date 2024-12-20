import os
import json
from natsort import os_sorted

# Config
base_path = "D:\\profile"


# End Config
def parse_directory(container, path):
    files = []
    folders = []
    for listed_file in os.listdir(path):
        if os.path.isdir(os.path.join(path, listed_file)):
            folders.append(listed_file)
        else:
            if listed_file.endswith(".rt4"):
                files.append(listed_file.removesuffix(".rt4"))
            elif listed_file.endswith(".txt"):
                files.append(listed_file)
    folder_len = len(files) + len(folders)
    folders = os_sorted(folders)
    files = os_sorted(files)
    files.sort()
    for index, found_file in enumerate(files):
        container[found_file] = {"name": found_file, "position": len(folders) + index, "length": folder_len}
    for index, folder in enumerate(folders):
        container[folder] = {"name": folder, "type": "folder", "position": index, "length": folder_len}
        parse_directory(container[folder], os.path.join(path, folder))


tree = {}
parse_directory(tree, base_path)
print(json.dumps(tree, indent=4))
with open("profiles.json", "w") as outfile:
    json.dump(tree, outfile)
with open("map.json", "w") as outfile:
    outfile.write("let map = ")
    json.dump(tree, outfile)
    outfile.write(";")

