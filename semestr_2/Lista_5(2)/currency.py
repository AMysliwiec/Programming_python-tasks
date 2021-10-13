from tkinter import *
from tkinter import ttk, messagebox
import requests
import copy
from PIL import Image, ImageTk
import time
import os
import json


def get_values(url=r"http://api.nbp.pl/api/exchangerates/tables/C/"):
    """
    :param url: important argument, without this link there would be no data
    :return: dictionary of currencies with their values in pln
    """
    resp = requests.get(url)
    data = resp.json()

    t = data[0]

    suff_data = t['rates']  # sufficient data c:
    code_list = ['PLN']
    value_list = [1.0]
    code_list.extend([suff_data[i]['code'] for i in range(len(suff_data))])
    value_list.extend([suff_data[i]['ask'] for i in range(len(suff_data))])

    complete_dictionary = {code_list[i]: value_list[i] for i in range(len(code_list))}
    return complete_dictionary


def first_access():
    """
    Function works without internet access, checks whether the computer has any dictionary with currencies saved
    :return: True - can work without internet, False - cannot work
    """
    with open('copy_of_data.txt', 'r') as file:
        line = file.read()
    file.close()

    if line == "":
        return False
    else:
        return True


def access(url=r"http://api.nbp.pl/api/exchangerates/tables/C/"):
    """
    Function overwrites the current exchange rates from url
    :param url: important argument, without this link there would be no data
    :return: date of the last modification of the file
    """
    copy_file = os.path.abspath('copy_of_data.txt')
    dictionary = get_values(url)

    with open(copy_file, 'w') as file:
        file.write(json.dumps(dictionary))
    file.close()

    mod_time = time.ctime(os.path.getmtime(copy_file))
    return mod_time


def check(url=r"http://api.nbp.pl/api/exchangerates/tables/C/"):
    """
    Depending on the access to the internet, function decides either it will download data from
    an archived file or current data from the internet
    :param url: important argument, without this link there would be no data
    :return: exchange rates in dictionary and date of the latest modification
    """
    try:
        dictionary = get_values(url)
    except requests.exceptions.ConnectionError:

        if not first_access():
            return "you do not have internet connection"
        else:
            currency_path = os.path.abspath('copy_of_data.txt')
            file = open(currency_path, 'r')
            last_dict = eval(file.read())
            mod_time = time.ctime(os.path.getmtime(currency_path))
            file.close()
            return last_dict, mod_time

    super_time = access(url)
    return dictionary, super_time


def converter():
    """
    The most beautiful code with tkinter
    """

    window = Tk()
    window.geometry('396x324')
    window.resizable(0, 0)
    window.title("Currency converter")

    information_nbp = check()
    currencies = information_nbp[0]
    if type(currencies) is not dict:
        messagebox.showerror(None, "No internet connection, cannot find any archival database of currencies")
        return

    dict_val = copy.deepcopy(currencies)
    get_time = information_nbp[1].split(" ")
    my_time = "{} {} {}".format(get_time[2], get_time[1], get_time[4])

    image = Image.open(r"C:\Users\Alutka\Desktop\Inglisz\money.jpg")
    image = image.resize((396, 324))
    image2 = ImageTk.PhotoImage(image)
    background_label = Label(window, image=image2)
    background_label.pack()

    amount_to_exchange = StringVar()

    firstLabel = Label(text="Entry: ", bg='aqua').place(x=25, y=120)
    entry_value = Entry(window, textvariable=amount_to_exchange, borderwidth=5)
    entry_value.place(x=127, y=120, width=140)

    currency = StringVar()
    currency2 = StringVar()

    combo_currency = ttk.Combobox(window, values=list(dict_val.keys()), textvariable=currency, state='readonly')
    combo_currency.place(x=26, y=85)

    combo_label = Label(text="Select an input currency  ", bg='grey', fg='black', font='Helvetica 8 bold italic')
    combo_label.place(x=27, y=65)

    combo_currency2 = ttk.Combobox(window, values=list(dict_val.keys()), textvariable=currency2, state='readonly')
    combo_currency2.place(x=223, y=85)

    combo_label2 = Label(text="Select an output currency", bg='grey', fg='black', font='Helvetica 8 bold italic')
    combo_label2.place(x=223, y=65)

    finalLabel = Label(text="Converted Amount :", bg='aqua').place(x=24, y=210)

    type_label = Label(text='', bg='grey', fg='black', width=7, height=2, font='Helvetica 10 bold italic')
    type_label.place(x=166, y=200)

    def exchange():
        """
        Function converts the indicated amount into the selected currency
        :return: result of exchange
        """
        your_amount = amount_to_exchange.get()
        val1 = currency.get()
        val2 = currency2.get()
        if val1 == val2:
            messagebox.showerror(None, "Converting means to change from one currency to the another")
        elif val1 not in dict_val.keys() or val2 not in dict_val.keys():
            messagebox.showerror(None, "To convert currencies selecting one of them is necessary")
        else:
            if your_amount == "":
                messagebox.showerror(None, "Surprisingly, 'nothing' has the same value everywhere")
            else:
                try:
                    your_amount = float(your_amount)
                except ValueError:
                    if "," in your_amount:
                        messagebox.showerror(None, "You need to enter a number,"
                                                   " check whether you put a comma instead of a dot")
                        return
                    else:
                        messagebox.showerror(None, "You need to enter a number")
                        return

                if your_amount < 0:
                    messagebox.showerror(None, "If you want to check how indebted you are, you don't need to enter"
                                               " an extra '-' before the number, enter a positive value")
                    return
                elif your_amount == 0:
                    messagebox.showerror(None, "No matter what country you fly to, 0 is always 0")
                    return
                else:
                    value_from = dict_val[val1]
                    value_to = dict_val[val2]
                    x = round((float(value_from) / float(value_to)) * your_amount, 2)
                    type_label.config(text=x)

    button_convert = Button(text="Convert", command=exchange)
    button_convert.place(x=170, y=155)

    def swap():
        """
        Function swaps the order of converting. For example:
        PLN -> EUR  'click on swap button'  EUR -> PLN
        """
        val1 = currency.get()
        val2 = currency2.get()
        if val1 == val2:
            messagebox.showerror(None, "What exactly do you want to achieve by doing this?")
        else:
            try:
                to_swap1 = list(dict_val.keys()).index(val1)
                to_swap2 = list(dict_val.keys()).index(val2)
            except ValueError:
                messagebox.showerror(None, "To swap currencies selecting two of them is necessary")
                return

            combo_currency.current(to_swap2)
            combo_currency2.current(to_swap1)

    button_swap = Button(text="Swap", command=swap)
    button_swap.place(x=177, y=85)

    def info():
        messagebox.showinfo("Help", "Welcome to a simple currency converter\n\nFirst select the currency with which "
                                    "you want to convert FROM, then select the one you want to convert TO\nNext: "
                                    "enter the amount you want to calculate in the designated place and use 'convert'"
                                    " button. \n\nExchange rates updated on: {}".format(my_time))

    button_help = Button(text="?", command=info, bg='grey', fg='white', width=7, height=2)
    button_help.place(x=335, y=236)

    def exit_bind(event):
        window.destroy()

    window.bind("<Escape>", exit_bind)

    button_quit = Button(text="EXIT", command=quit, bg='red', fg='white', width=7, height=2)
    button_quit.place(x=335, y=280)

    window.mainloop()


if __name__ == "__main__":
    converter()
