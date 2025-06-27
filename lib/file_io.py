# lib/file_io.py

def write_file(file_name, file_content):
    with open(f"{file_name}.txt", mode='w') as file:
        file.write(file_content)


def append_file(file_name, file_content):
    with open(f"{file_name}.txt", mode='a') as file:
        file.write(file_content)


def read_file(file_name):
    with open(f"{file_name}.txt", mode='r') as file:
        return file.read()
