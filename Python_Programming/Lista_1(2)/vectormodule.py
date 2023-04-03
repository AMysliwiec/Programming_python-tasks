import random
import math as m


class Vector:
    """
    This class is used to represent a vector with a specific dimension (the number of coordinates)
    """

    def __init__(self, n: int = 3):
        """
        Creating a null vector according to its own dimension, self.c is a digest for longer form - self.coordinates
        :param n: the number of coordinates
        """
        if n > 0:
            self.n = n
            self.c = []
            for i in range(self.n):
                self.c.append(0)
        else:
            raise ValueError("The dimension shall not be less than zero")

    def random_values(self):
        """
        Function assigns random coordinates to a vector
        """
        for i in range(self.n):
            a = random.randint(-10, 10)
            self.c[i] = a

    def from_list(self, lista: list):
        """
        Function assigns coordinates to a vector from a list which is an argument of
        :param lista: list of desired coordinates
        """
        if len(lista) == self.n:
            for ele in lista:
                if type(ele) != int:
                    raise ValueError("Each coordinate must be an integer")
                else:
                    pass
            self.c = lista
        else:
            raise ValueError("the list must be consistent with the dimension of the object")

    def __add__(self, other):
        """
        An operator that adds the coordinates of two vectors
        :param other: another object of class Vector
        :return: a new vector with the created coordinates
        """
        if self.n == other.n:
            my_sum = []
            for i in range(self.n):
                eleInSum = self.c[i] + other.c[i]
                my_sum.append(eleInSum)
            return my_sum
        else:
            raise ValueError("Vectors must be the same size")

    def __sub__(self, other):
        """
        An operator which subtracts the coordinates of two vectors
        :param other: another object of class Vector
        :return: a new vector with the created coordinates
        """
        if self.n == other.n:
            diff = []
            for i in range(self.n):
                eleInDiff = self.c[i] - other.c[i]
                diff.append(eleInDiff)
            return diff
        else:
            raise ValueError("Vectors must be the same size")

    def __mul__(self, scalar):
        """
        An operator which multiplies each coordinate of a vector by the specified scalar
        :param scalar: desired scalar
        :return: multiplied vector
        """
        result_mul = [x * scalar for x in self.c]
        return result_mul

    def __rmul__(self, scalar):
        """
        An operator which multiplies each coordinate of a vector by the specified scalar
        :param scalar: desired scalar
        :return: multiplied vector
        """
        result_rmul = [x * scalar for x in self.c]
        return result_rmul

    def vec_len(self):
        """
        Function counts the length of a vector
        :return: length of a vector
        """
        result_sum = 0
        check_sum = 0
        for i in self.c:
            if i == 0:
                check_sum += 1
        if check_sum == len(self.c):
            raise ValueError("Empty vector")
        else:
            for i in range(self.n):
                sum_element = self.c[i] ** 2
                result_sum += sum_element
            length = m.sqrt(result_sum)
            return round(length, 3)

    def elem_sum(self):
        """
        Function sums all coordinates of a vector
        :return: the result of adding each element
        """
        sum_of_elements = 0
        for i in range(self.n):
            sum_of_elements += self.c[i]
        return sum_of_elements

    def scalar_prod(self, other):
        """
        Function counts the scalar product of a vector with another object of class Vector
        :param other: another object of class Vector
        :return: excact scalar product
        """
        product = 0
        if self.n == other.n:
            for i in range(self.n):
                product += self.c[i] * other.c[i]
            return product
        else:
            raise ValueError("Vectors must be the same size")

    def __str__(self):
        """
        Operator returns the text representation of a vector
        :return: a list of specific coordinates
        """
        return str(self.c)

    def __getitem__(self, index: int):
        """
        Operator looks for one or more elements of a vector using subscripts
        :param index: the index/indices we want to check
        :return: the coordinates on the index you are looking for
        """
        try:
            return self.c[index]
        except IndexError:
            raise ValueError("Cannot find such an index")
        except TypeError:
            raise ValueError("The index number must be an integer")

    def __contains__(self, item: int):
        """
        Operator checks if the specified element belongs to the vector
        :param item: the element you are looking for
        :return: True if the function finds a given number, otherwise False
        """
        return item in self.c
