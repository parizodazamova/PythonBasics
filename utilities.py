def write_txt_file(file_path, lines, mode="a"):
    """
    Writes to list of inputs as lines to a given file path.
    :param file_path: absolute or relative path of the file
    :param lines: list of information, in the form of list DS
    :return: file object
    """
    with open(file_path, mode=mode) as file_obj:
        for line in lines:
            file_obj.write(line)

def read_yaml_file(file_path):
    """
    Reads yaml type files (configuration files)
    :param file_path: abs or relative path
    :return:
    """
    with open(customers_path, 'r') as file:
    customers = yaml.safe_load(file)
    data = yaml.safe_load(file)
    return data
