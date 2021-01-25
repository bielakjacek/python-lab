import os

for root, dirs, files in os.walk(".\\dev", topdown=True):
    for file_name in files:
        print(os.path.join(root, file_name))
    for dir_name in dirs:
        print(os.path.join(root, dir_name))
