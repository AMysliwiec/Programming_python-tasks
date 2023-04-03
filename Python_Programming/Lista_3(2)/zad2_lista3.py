import os
import sys


def zad2(current_path: str):
    """
    Function unpacks the given directory if possible and removes the empty directory
    :param current_path: path to the folder to be unpacked (entered as 'r + path'!)
    """

    if os.path.exists(current_path):
        if os.path.isdir(current_path):
            path_to_unpack = os.path.dirname(current_path)

            list_of_files = os.listdir(current_path)

            if len(list_of_files) == 0:
                raise ValueError("Nothing to unpack")
            else:
                for file in list_of_files:
                    os.replace(current_path + "\\{}".format(file), path_to_unpack + "\\{}".format(file))

                if len(os.listdir(current_path)) == 0:
                    os.rmdir(current_path)
        else:
            raise TypeError("It is impossible to unpack anything else than a folder")
    else:
        raise FileNotFoundError("Cannot find the directory")


if __name__ == "__main__":
    if len(sys.argv) > 2:
        print("Function needs only one argument")
    else:
        zad2(sys.argv[1])
