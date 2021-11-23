def ordinary_polynomial_value_calc(coeff, arg):
    """
    Function counts the value of the polynomial and returns the number of additions and multiplications made
    :param coeff: a list of factors starting with the intercept
    :param arg: the argument for which we are calculating the value
    :return: value, number of multiplications, -||- additions
    """
    length = len(coeff)

    count_mult, count_add, value = 0, length - 1, coeff[0]
    step = 1

    if arg == 0:
        count_add = 0
        return value, count_mult, count_add

    if coeff[0] == 0:
        count_add -= 1

    for i in coeff[1:]:
        if arg == 1:
            if i == 0:
                count_add -= 1
            else:
                value += i
        else:
            if i == 0:
                count_add -= 1
            elif i == 1:
                value += arg ** step
                count_mult += step - 1
            else:
                value += i * (arg ** step)
                count_mult += step
            step += 1

    return value, count_mult, count_add


def smart_polynomial_value_calc(coeff, arg):
    """
    Function counts the value of the polynomial using Horner's Rule and returns the number of additions
    and multiplications made
    :param coeff: a list of factors starting with the intercept
    :param arg: the argument for which we are calculating the value
    :return: value, number of multiplications, -||- additions
    """
    count_mult, count_add, value = 0, 0, coeff[-1]
    coeff.reverse()

    if arg == 0:
        value = coeff[-1]
        return value, count_mult, count_add

    for i in coeff[1:]:
        if arg == 1:
            if i == 0:
                pass
            else:
                value += i
                count_mult += 1
        else:
            if i == 0:
                value *= arg
                count_mult += 1
            else:
                value = value * arg + i
                count_mult += 1
                count_add += 1

    return value, count_mult, count_add
