#!/usr/bin/python

import os

# Config
base_path = "c:\\profiles"

# End Config

result ={}

# traverse root directory, and list directories as dirs and files as files
for root, dirs, files in os.walk(base_path):
    if root == base_path:
        continue
    print(root)
    dir_count = 0
    for dir in dirs :
        result[dir]=0
    print(dirs)
    print(files)
    print('--------------------------------')
