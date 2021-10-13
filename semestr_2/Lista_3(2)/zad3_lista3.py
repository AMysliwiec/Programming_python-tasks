import os
import shutil
import time
import datetime
import sys


def zad3(catalog: str, place_to_save: str, extensions: list):
    """
    Function looks for files with given extensions in certain directories. Then creates backups of those modified
    in the last three days to 'Backup\\copy-{current date}' directory.
    !All paths need to be entered as 'r + path'!
    :param catalog: directory path that is to be searched
    :param place_to_save: directory path where the final backup is to be placed
    :param extensions: wanted extensions (for example: [".txt", ".jpg", ...])
    """

    if os.path.exists(catalog):
        if os.path.exists(place_to_save):
            THREE_DAYS = 24 * 3 * 60 * 60
            current_time = time.time()
            timestamp = current_time - THREE_DAYS

            list_of_files = []
            for root, dirs, files in os.walk(catalog, topdown=True):
                for ele in files:
                    if os.path.splitext(ele)[-1] in extensions:
                        file = str(os.path.join(root, ele))
                        filetime = os.path.getmtime(file)
                        if filetime > timestamp:
                            list_of_files.append(file)
                        else:
                            continue
                    else:
                        continue

            current_date = str(datetime.date.today())
            backup_dir = os.path.join(place_to_save, r"Backup\copy-{}".format(current_date))

            try:
                os.makedirs(backup_dir)
            except FileExistsError:
                pass

            os.chdir(backup_dir)

            for item in list_of_files:
                shutil.copy2(item, backup_dir)
        else:
            raise FileNotFoundError("Cannot find wanted directory")
    else:
        raise FileNotFoundError("Your path does not exist")


if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Function needs more arguments")
    else:
        zad3(sys.argv[1], sys.argv[2], sys.argv[3:])
