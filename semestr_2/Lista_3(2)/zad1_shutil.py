import os
import sys
from shutil import copy2
from exist_check import file_exist


def zad1_shutil(files: list, dir_name: str, place_to_save: str):
    """
    Function makes copies of .txt files and packs them into a folder with chosen name
    :param files: list of the file paths
    :param dir_name: name of the folder with these copies
    :param place_to_save: directory path where the above-mentioned folder is to be placed
    """

    list_of_files = file_exist(files)

    if os.path.exists(place_to_save):
        dest_path = os.path.join(place_to_save, dir_name)
    else:
        raise FileNotFoundError("Cannot find wanted directory")

    try:
        os.mkdir(dest_path)
    except FileExistsError:
        pass

    for text_file in list_of_files:
        if os.path.splitext(text_file)[-1] == ".txt":
            copy2(text_file, dest_path)
        else:
            raise TypeError("Extension of the files must be a '.txt'")


if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Function needs more arguments")
    else:
        zad1_shutil(sys.argv[1:-2], sys.argv[-2], sys.argv[-1])
