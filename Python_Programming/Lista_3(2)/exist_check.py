import os


def file_exist(files: list):
    """
    Function checks whether a file exists or not
    :param files: list of path files
    :return: given list as long as everything is correct
    """

    test_list = []
    for file in files:
        if os.path.exists(file):
            test_list.append(file)
        else:
            pass

    if files == test_list:
        return files
    else:
        raise FileNotFoundError("Wrong file paths")
