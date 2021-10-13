import os
import time

startdir = r"C:\Users\Alutka\Desktop\notimportant"


def generate_stats(catalog_name: str):
    """
    Function generates the last file modifications up to a year ago from the selected directory on the computer
    :param catalog_name: path to the selected folder
    :return: list of the result of stats
    """
    if os.path.exists(catalog_name):
        YEAR_IN_SEC = 365 * 24 * 60 * 60
        timestamp = time.ctime(YEAR_IN_SEC)
        list_of_stats = []
        for root, dirs, files in os.walk(catalog_name, topdown=True):
            for ele in files:
                file = str(os.path.join(root, ele))
                filetime = time.ctime(os.path.getmtime(file))
                if filetime > timestamp:
                    stat = " {} - Last modified: {}".format(ele, filetime)
                    list_of_stats.append(stat)
                else:
                    continue
        return list_of_stats
    else:
        raise FileNotFoundError("Your path does not exist!")


def show_me_stats(catalog_name: str):
    """
    Function prints the stats from "generate_stats" function
    :param catalog_name: path to the selected folder
    :return: stats
    """
    stats = generate_stats(catalog_name)
    for ele in stats:
        print(ele, "\n", 100 * "-")


show_me_stats(startdir)
