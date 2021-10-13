from math import floor
import calendar


def compute_Easter_date(year: int = 1990):
    """
    Function calculate the exact day of Easter Sunday
    :param year: the year we want to check the above-mentioned date
    :return: list [day: number of the day of the week, month: number of the month]
    """
    if year <= 0:
        raise ValueError("Easter was not celebrated before our era")
    else:
        a = year % 19
        b = floor(year / 100)
        c = year % 100
        d = floor(b / 4)
        e = b % 4
        f = floor((b + 8) / 25)
        g = floor((b - f + 1) / 3)
        h = (19 * a + b - d - g + 15) % 30
        i = floor(c / 4)
        k = c % 4
        l = (32 + 2 * e + 2 * i - h - k) % 7
        m = floor((a + 11 * h + 22 * l) / 451)
        p = (h + l - 7 * m + 114) % 31
        day = p + 1
        month = floor((h + l - 7 * m + 114) / 31)
        return [day, month]


def tell_me_Easter_date(year):
    """
    Function generates a string with the date of Easter
    :param year: the year we want to check
    :return: information about the date
    """
    data = compute_Easter_date(year)
    easter_month = calendar.month_name[data[1]]
    return "The date of Easter Sunday in {}:\n {} {}".format(year, data[0], easter_month)


print(tell_me_Easter_date(2021))
