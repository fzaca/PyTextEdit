def read_file(file_path):
    with open(file_path, 'r') as f:
        file = f.read()
    return file

def write_file(file_path, text):
    with open(file_path, 'w') as f:
        f.write(text)
