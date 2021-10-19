from math import gcd


# ------------------- HELPER FUNCTION --------------------------


def verify_one_type(value):
    """
    Function checks if the entered value type is compatible to Fraction class
    """

    if not isinstance(value, Fraction):
        raise TypeError("Invalid type! You can only operate with fractions")

    pass


# ------------------- PROPER CODE --------------------------


class Fraction:
    """
    Class to make fractions
    """

    constant = 2

    @staticmethod
    def mixed(element):
        """
        It's a static method that allows us to set a fraction appearance function
        :param element: if 'True' we get mixed fraction, 'False' - simple
        """

        if element == "True":
            Fraction.constant = 3

        elif element == "False":
            Fraction.constant = 2

        else:
            raise TypeError("The argument must be 'True' or 'False'")

    def __init__(self, numerator, denominator):

        if denominator == 0:
            raise ZeroDivisionError("Cannot create a fraction with 0 as a denominator")

        if type(numerator) is not int or type(denominator) is not int:
            raise TypeError("Numerator and denominator must be integers")

        number = gcd(numerator, denominator)
        self.num = numerator // number
        self.den = denominator // number

        if self.num < 0 and self.den < 0 or self.den < 0:
            self.num *= -1
            self.den *= -1

        self.approx = self.num / self.den

    def __add__(self, other):
        """
        :return: result, fraction class object
        """

        verify_one_type(other)

        if self.den == other.den:

            new_den = self.den
            new_num = self.num + other.num

        else:

            new_den = self.den * other.den
            new_num = self.num * other.den + other.num * self.den

        return Fraction(new_num, new_den)

    def __sub__(self, other):
        """
        :return: result, fraction class object
        """

        verify_one_type(other)

        if self.den == other.den:

            new_den = self.den
            new_num = self.num - other.num

        else:

            new_den = self.den * other.den
            new_num = self.num * other.den - other.num * self.den

        return Fraction(new_num, new_den)

    def __mul__(self, other):
        """
        :return: result, fraction class object
        """

        verify_one_type(other)

        new_num = self.num * other.num
        new_den = self.den * other.den

        return Fraction(new_num, new_den)

    def __truediv__(self, other):
        """
        :return: result, fraction class object
        """

        verify_one_type(other)

        if other.num == 0:
            raise ZeroDivisionError("Cannot be divided by zero :c")

        new_num = int(self.num * other.den)
        new_den = int(self.den * other.num)

        return Fraction(new_num, new_den)

    def __neg__(self):

        new_num = self.num * -1

        return Fraction(new_num, self.den)

    def __lt__(self, other):

        verify_one_type(other)

        if self.approx < other.approx:
            return True
        else:
            return False

    def __gt__(self, other):

        verify_one_type(other)

        if self.approx > other.approx:
            return True
        else:
            return False

    def __le__(self, other):

        verify_one_type(other)

        if self.approx <= other.approx:
            return True
        else:
            return False

    def __ge__(self, other):

        verify_one_type(other)

        if self.approx >= other.approx:
            return True
        else:
            return False

    def __eq__(self, other):

        verify_one_type(other)

        if self.approx == other.approx:
            return True
        else:
            return False

    def __ne__(self, other):

        verify_one_type(other)

        if self.approx != other.approx:
            return True
        else:
            return False

    def __str__(self):
        """
        Function represents the appearance of the fraction
        :return: depending on how 'mixed' method is set, either simple or mixed fraction is returned
        """

        if abs(self.num) == abs(self.den) or self.den == 1:
            return "{}".format(int(self.num))

        if Fraction.constant == 3 and abs(self.num) > self.den:
            big_number = int(abs(self.num) // self.den)
            new_num = int(abs(self.num) % self.den)

            if self.num < 0:
                big_number *= -1

            return "{}({}/{})".format(big_number, new_num, self.den)

        else:

            return "{}/{}".format(int(self.num), int(self.den))

    def get_num(self):
        """
        :return: Numerator
        """

        return self.num

    def get_den(self):
        """
        :return: Denominator
        """

        return self.den
