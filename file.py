# file_utils.py
import os

def create_file(filename):
    if os.path.exists(filename):
        os.remove(filename)

def append_to_file(filename, content):
    with open(filename, "a") as file:
        file.write(content)
