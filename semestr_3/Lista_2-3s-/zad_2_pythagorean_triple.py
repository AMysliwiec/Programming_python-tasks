"""
This file contains functions for finding Pythagorean triplets and its subsequent step-by-step optimizations.
A function with parameterization is also implemented. 'l' is standing for number such that the triplet elements
- a, b and c - sum up to this number. 'operations' are to count the operations performed to find the triplet.
"""


def pythagorean_triple_1(l):
    operations = 0
    for a in range(1, l):
        for b in range(1, l):
            for c in range(1, l):
                operations += 9
                if a ** 2 + b ** 2 == c ** 2 and a + b + c == l:
                    return True, [a, b, c], operations

    return False, [-1, -1, -1], operations


def pythagorean_triple_2(l):
    operations = 0
    for a in range(1, l):
        for b in range(a + 1, l):
            for c in range(b + 1, l):
                operations += 11
                if a ** 2 + b ** 2 == c ** 2 and a + b + c == l:
                    return True, [a, b, c], operations

    return False, [-1, -1, -1], operations


def pythagorean_triple_3(l):
    operations = 0
    for a in range(1, l):
        for b in range(a + 1, l):
            for c in range(b + 1, a + b):
                operations += 12
                if a ** 2 + b ** 2 == c ** 2 and a + b + c == l:
                    return True, [a, b, c], operations

    return False, [-1, -1, -1], operations


def pythagorean_triple_4(l):
    operations = 0
    for a in range(1, l):
        for b in range(a + 1, l):
            c = l - a - b
            operations += 8
            if a ** 2 + b ** 2 == c ** 2:
                return True, [a, b, c], operations

    return False, [-1, -1, -1], operations


def pythagorean_triple_5(l):
    operations = 0
    for a in range(1, l):
        b = int((l ** 2 - 2 * a * l) / (2 * (l - a)))
        c = l - a - b
        operations += 16
        if a ** 2 + b ** 2 == c ** 2 and b > a:
            return True, [a, b, c], operations

    return False, [-1, -1, -1], operations


def pythagorean_triple_6(l):
    limit = l // 3
    operations = 1
    for a in range(1, limit):
        b = int((l ** 2 - 2 * a * l) / (2 * (l - a)))
        c = l - a - b
        operations += 16
        if a ** 2 + b ** 2 == c ** 2:
            return True, [a, b, c], operations

    return False, [-1, -1, -1], operations


# ---------------- PARAMETRIZATION ---------------------


def primary_pythagorean_triple_parametric(l):
    """
    The function searches for Pythagorean triples such that their sum is equal to a given number.
    It is only capable of finding primal triplets (non-abbreviated)
    :param l: we look for a, b and c such that a + b + c = l
    :return:if found - True, [a, b, c], number of operations that were performed to find the triplet,
    if not - False, [-1, -1, -1] and all operations performed
    """

    n, c, operations = 1, 1, 0
    list_true, list_false = [True], [False, [-1, -1, -1]]

    while c < l:
        for m in range(1, n):
            a = n ** 2 - m ** 2
            b = 2 * m * n
            c = n ** 2 + m ** 2

            sum = a + b + c
            operations += 11

            if sum == l:
                list_of_numbers = [a, b, c]
                list_of_numbers.sort()

                for ele in [list_of_numbers, operations]:
                    list_true.append(ele)
                return list_true

        operations += 1
        n += 1

    list_false.append(operations)
    return list_false


def pythagorean_triple_parametric(l):
    """
    Basically as above, the function has been enhanced to recognize and find any Pythagorean triple
    - not only the primal one
    """

    n, c, operations = 1, 1, 0
    list_true, list_false = [True], [False, [-1, -1, -1]]

    while c < l:
        for m in range(1, n):
            a = n ** 2 - m ** 2
            b = 2 * m * n
            c = n ** 2 + m ** 2

            sum = a + b + c
            operations += 12
            if l % sum == 0:

                factor = l // sum
                if factor != 0:
                    operations += 5

                    list_of_numbers = [a * factor, b * factor, c * factor]
                    list_of_numbers.sort()

                    for ele in [list_of_numbers, operations]:
                        list_true.append(ele)
                    return list_true

        operations += 1
        n += 1

    list_false.append(operations)
    return list_false


# ----------------------- ALL TRIPLES ----------------------------


def all_pythagorean_triple(l):
    """
    This function finds all the possible pythagorean triples
    """
    operations, triplets = 0, []
    for a in range(1, l // 3):
        b = int((l ** 2 - 2 * a * l) / (2 * (l - a)))
        c = l - a - b
        operations += 14
        if a ** 2 + b ** 2 == c ** 2:
            triplets.append([a, b, c])

    if len(triplets) == 0:
        return False, [-1, -1, -1], operations
    return True, triplets, operations
