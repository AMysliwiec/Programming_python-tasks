from PIL import Image
import os


def generate_miniature_jpg(catalog_name: str, size: list,
                           file_name_out: str, destiny_catalog: str = r"C:\Users\Alutka\Desktop\Miniatures"):
    """
    Function generates a miniature of any picture
    :param catalog_name: path to the picture
    :param size: desired size of the miniature [width, height]
    :param file_name_out: name of the file with saved miniature with the extension .jpg
    :param destiny_catalog: path to the place where you want to save the miniature
    :return: feedback whether it was successful
    """
    if os.path.exists(catalog_name):
        if os.path.exists(destiny_catalog):
            os.chdir(destiny_catalog)
            if len(size) != 2:
                raise IndexError("Picture has two measurements")
            else:
                image = Image.open(catalog_name)
                if image.size[0] <= size[0] or image.size[1] <= size[1]:
                    raise ValueError("It definitely won't be a MINIATURE")
                else:
                    new_image = image.resize((size[0], size[1]))
                    new_image.save(file_name_out)
                    image.show()
                    new_image.show()
                    return "Enjoy your beautiful miniature"
        else:
            raise FileNotFoundError("Cannot save the picture in this location")
    else:
        raise FileNotFoundError("Your path does not exist!")


zdjecie = r"C:\Users\Alutka\Desktop\notimportant\Zdjatka\tlo balony.jpg"
print(generate_miniature_jpg(zdjecie, [200, 100], 'zdjecieee.jpg'))
