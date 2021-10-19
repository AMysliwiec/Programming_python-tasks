from math import gcd


# ------------------- HELPER FUNCTIONS --------------------------


def how_many(number: float):
    """
    Function checks the number of decimal places
    :param number: Number to check
    """
    return len(str(number).split(".")[1])


def float_to_integer(a, b):
    """
    Function moves the comma of the numbers to get an integers
    :return: Changed numbers
    """

    if type(a) not in [int, float] or type(b) not in [int, float]:
        raise TypeError("Given numbers must be either integers or floats")

    number_1, number_2 = 0, 0

    if type(a) is float:
        number_1 = how_many(a)
    if type(b) is float:
        number_2 = how_many(b)

    if number_1 == 0 and number_2 == 0:
        pass

    elif number_1 == 0 or number_1 < number_2:
        a *= (10 ** number_2)
        b *= (10 ** number_2)

    elif number_2 == 0 or number_1 >= number_2:
        b *= (10 ** number_1)
        a *= (10 ** number_1)

    return [int(a), int(b)]


def verify_type(value):
    """
    Function checks if the entered value type is compatible to ExtremeFraction class
    """

    if not isinstance(value, (int, float, ExtremeFraction)):
        raise TypeError("Invalid type! try to operate with numbers or other fractions")

    pass

# -------------------------------- PROPER CODE --------------------------------------


class ExtremeFraction:
    """
    Class to make fractions even with floats as an argument
    """

    constant = 1.5

    @staticmethod
    def mixed(element):
        """
        It's a static method that allows us to set a fraction appearance function
        :param element: if 'True' we get mixed fraction, 'False' - simple
        """

        if element == "True":
            ExtremeFraction.constant = 2.5

        elif element == "False":
            ExtremeFraction.constant = 1.5

        else:
            raise TypeError("The argument must be 'True' or 'False'")

    def __init__(self, numerator, denominator):

        if denominator == 0:
            raise ZeroDivisionError("Cannot create a fraction with 0 as a denominator")

        new_ints = float_to_integer(numerator, denominator)
        numerator, denominator = new_ints[0], new_ints[1]

        number = gcd(numerator, denominator)
        self.num = int(numerator // number)
        self.den = int(denominator // number)

        if self.num < 0 and self.den < 0 or self.den < 0:
            self.num *= -1
            self.den *= -1

        self.approx = self.num / self.den

    def __add__(self, other):
        """
        :return: result, fraction class object
        """

        verify_type(other)

        if isinstance(other, (int, float)):

            new_den = self.den
            new_num = self.num + other * self.den

        elif self.den == other.den:

            new_den = self.den
            new_num = self.num + other.num

        else:

            new_den = self.den * other.den
            new_num = self.num * other.den + other.num * self.den

        return ExtremeFraction(new_num, new_den)

    def __radd__(self, other):
        """
        :return: result, fraction class object
        """

        verify_type(other)

        if isinstance(other, (int, float)):

            new_den = self.den
            new_num = self.num + other * self.den

        elif self.den == other.den:

            new_den = self.den
            new_num = self.num + other.num

        else:

            new_den = self.den * other.den
            new_num = self.num * other.den + other.num * self.den

        return ExtremeFraction(new_num, new_den)

    def __sub__(self, other):
        """
        :return: result, fraction class object
        """

        verify_type(other)

        if isinstance(other, (int, float)):

            new_den = self.den
            new_num = self.num - other * self.den

        elif self.den == other.den:

            new_den = self.den
            new_num = self.num - other.num

        else:

            new_den = self.den * other.den
            new_num = self.num * other.den - other.num * self.den

        return ExtremeFraction(new_num, new_den)

    def __rsub__(self, other):
        """
        :return: result, fraction class object
        """

        verify_type(other)

        if isinstance(other, (int, float)):

            new_den = self.den
            new_num = other * self.den - self.num

        elif self.den == other.den:

            new_den = self.den
            new_num = other.num - self.num

        else:

            new_den = self.den * other.den
            new_num = other.num * self.den - self.num * other.den

        return ExtremeFraction(new_num, new_den)

    def __mul__(self, other):
        """
        :return: result, fraction class object
        """

        verify_type(other)

        if isinstance(other, (int, float)):

            new_num = self.num * other
            new_den = self.den

        else:
            new_num = self.num * other.num
            new_den = self.den * other.den

        return ExtremeFraction(new_num, new_den)

    def __rmul__(self, other):
        """
        :return: result, fraction class object
        """

        verify_type(other)

        if isinstance(other, (int, float)):

            new_num = self.num * other
            new_den = self.den

        else:
            new_num = self.num * other.num
            new_den = self.den * other.den

        return ExtremeFraction(new_num, new_den)

    def __truediv__(self, other):
        """
        :return: result, fraction class object
        """

        verify_type(other)

        if isinstance(other, (int, float)):

            if other == 0:
                raise ZeroDivisionError("Cannot be divided by zero :c")

            new_num = self.num
            new_den = self.den * other

        else:
            if other.num == 0:
                raise ZeroDivisionError("Cannot be divided by zero :c")

            new_num = int(self.num * other.den)
            new_den = int(self.den * other.num)

        return ExtremeFraction(new_num, new_den)

    def __rtruediv__(self, other):
        """
        :return: result, fraction class object
        """

        verify_type(other)

        if isinstance(other, (int, float)):

            if other == 0:
                raise ZeroDivisionError("Cannot be divided by zero :c")

            new_num = self.den * other
            new_den = self.num

        else:
            if other.num == 0:
                raise ZeroDivisionError("Cannot be divided by zero :c")

            new_num = int(self.den * other.num)
            new_den = int(self.num * other.den)

        return ExtremeFraction(new_num, new_den)

    def __neg__(self):

        new_num = self.num * -1

        return ExtremeFraction(new_num, self.den)

    def __lt__(self, other):

        verify_type(other)

        if isinstance(other, (int, float)):

            if self.approx < other:
                return True
            else:
                return False

        if self.approx < other.approx:
            return True
        else:
            return False

    def __gt__(self, other):

        verify_type(other)

        if isinstance(other, (int, float)):

            if self.approx > other:
                return True
            else:
                return False

        if self.approx > other.approx:
            return True
        else:
            return False

    def __le__(self, other):

        verify_type(other)

        if isinstance(other, (int, float)):

            if self.approx <= other:
                return True
            else:
                return False

        if self.approx <= other.approx:
            return True
        else:
            return False

    def __ge__(self, other):

        verify_type(other)

        if isinstance(other, (int, float)):

            if self.approx >= other:
                return True
            else:
                return False

        if self.approx >= other.approx:
            return True
        else:
            return False

    def __eq__(self, other):

        verify_type(other)

        if isinstance(other, (int, float)):

            if self.approx == other:
                return True
            else:
                return False

        if self.approx == other.approx:
            return True
        else:
            return False

    def __ne__(self, other):

        verify_type(other)

        if isinstance(other, (int, float)):

            if self.approx != other:
                return True
            else:
                return False

        if self.approx != other.approx:
            return True
        else:
            return False

    def __str__(self):
        """
        Function represents the appearance of the fraction
        :return: depending on how 'mixed' method is set, either simple or mixed fraction is returned
        """

        if ExtremeFraction.constant == 2.5 and abs(self.num) > self.den:
            big_number = int(abs(self.num) // self.den)
            new_num = int(abs(self.num) % self.den)

            if self.num < 0:
                big_number *= -1

            return "{}({}/{})".format(big_number, new_num, self.den)

        if abs(self.num) == abs(self.den) or self.den == 1:
            return "{}".format(int(self.num))
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
