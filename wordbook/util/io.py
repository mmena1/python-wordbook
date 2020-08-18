def read_file(input_file):
    """
    Can take a file path or a IO stream.
    """
    file = None
    try:
        if isinstance(input_file, str):
            file = open(input_file)
        else:
            file = input_file
        return file.read()
    finally:
        if file:
            file.close()


def write_file(contents, output_path):
    """
    Can take a file path or a IO stream.
    """
    file = None
    try:
        if isinstance(output_path, str):
            file = open(output_path, "w")
        else:
            file = output_path
        file.write(contents)
    finally:
        if file:
            file.close()
