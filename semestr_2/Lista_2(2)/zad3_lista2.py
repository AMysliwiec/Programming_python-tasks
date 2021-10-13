from zipfile import ZipFile
import datetime
import os


def generate_zip_copy(catalog_name: str, destiny_catalog: str = r"C:\Users\Alutka\Desktop\Zipki"):
    """
    Function creates a zip with a copy of the selected folder from path
    :param catalog_name: path to the selected folder
    :param destiny_catalog: path to the place where you want to save the zip
    :return: feedback whether it was successful
    """
    if os.path.exists(catalog_name):
        if os.path.exists(destiny_catalog):
            os.chdir(destiny_catalog)
            catalog = catalog_name.split("\\")
            current_date = str(datetime.date.today())
            name = "{}_{}_backup.zip".format(current_date, catalog[-1])
            with ZipFile(name, "w") as safety_zip:
                for root, dirs, files in os.walk(catalog_name):
                    for filename in files:
                        file = os.path.join(root, filename)
                        safety_zip.write(file)
            return "Successfully compressed to a zip"
        else:
            raise FileNotFoundError("Cannot save zip in this location")
    else:
        raise FileNotFoundError("Your path does not exist!")


print(generate_zip_copy(r"C:\Users\Alutka\Desktop\notimportant"))
