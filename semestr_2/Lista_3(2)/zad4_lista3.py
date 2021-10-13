import sys
import os


def zad4(path_file: str):
    """
    Function changes the characteristic end lines in .txt files from Windows to Unix and vice versa.
    If end lines are from Macintosh, function converts them to Windows.
    :param path_file: .txt file path (entered as 'r + path'!)
    """

    if os.path.exists(path_file):
        if os.path.isfile(path_file):

            if os.path.splitext(path_file)[-1] == ".txt":
                WINDOWS_LINE = b"\r\n"
                UNIX_LINE = b"\n"
                MACINTOSH_LINE = b"\r"

                file = open(path_file, "rb")
                lines = file.readlines()
                if WINDOWS_LINE in lines[0]:
                    lines = [line.replace(WINDOWS_LINE, UNIX_LINE) for line in lines]
                elif UNIX_LINE in lines[0]:
                    lines = [line.replace(UNIX_LINE, WINDOWS_LINE) for line in lines]
                elif MACINTOSH_LINE in lines[0]:
                    lines = [line.replace(MACINTOSH_LINE, WINDOWS_LINE) for line in lines]
                file.close()

                changed_file = open(path_file, "wb")
                changed_file.writelines(lines)
                changed_file.close()
            else:
                raise ValueError("Extension of the file must be a '.txt'")
        else:
            raise TypeError("Argument must be a file")
    else:
        raise FileNotFoundError("No such file or directory")


if __name__ == "__main__":
    if len(sys.argv) > 2:
        print("Function needs only one argument")
    else:
        zad4(sys.argv[1])
