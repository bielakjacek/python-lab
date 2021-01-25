import os

directory = ".\\"
file_to_convert = [file for file in os.listdir(directory) if os.path.isfile(os.path.join(directory, file))]


def jpg_to_png():
    for file in file_to_convert:
        os.rename(file, file.replace(".jpg", ".png"))


def png_to_jpg():
    for file in file_to_convert:
        os.rename(file, file.replace(".png", ".jpg"))


jpg_to_png()
# png_to_jpg()
