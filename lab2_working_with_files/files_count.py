import os.path


directory = ".\\dev"
print(len([file for file in os.listdir(directory) if os.path.isfile(os.path.join(directory, file))]))
