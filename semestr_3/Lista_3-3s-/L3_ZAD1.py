def binomial_coeff(n, k):
    """
    Function counts the binomial coefficient from given numbers
    :param n: upper number
    :param k: lower number
    :return: value, number of multiplications
    """
    result, end, count_mult = 1, k + 1, 0

    for i in range(1, end):
        result *= (n - i + 1) / i
        count_mult += 2
    return result, count_mult


def to_any_pow(base, any_pow):
    """
    Function counts the value of base raised to a given power
    :param base: the foundation of power
    :param any_pow: power
    :return: value, number of multiplications
    """
    count_mult, result = 0, 1

    if any_pow < 12:
        result = base ** any_pow
        count_mult += any_pow - 1

        return result, count_mult

    while any_pow > 0:
        if any_pow % 2 == 0:
            any_pow //= 2
            base *= base
            count_mult += 2
        else:
            any_pow = (any_pow - 1) // 2
            result *= base
            base *= base
            count_mult += 3

    return result, count_mult


def probability(n, k, p):
    """
    Function calculates the probability of achieving at most k successes
    :param n: number of tries
    :param k: maximum number of successes
    :param p: probability of a single succes
    :return: probability, number of multiplications
    """
    count_mult, prob = 1, 0
    iter_list = [it for it in range(0, k + 1)]
    p_elem = p / (1 - p)
    data = to_any_pow((1 - p), n)
    data_value = data[0]

    if n == k:
        return 1, 0

    for i in iter_list:
        newton_step = binomial_coeff(n, i)
        func = newton_step[0] * data_value
        prob += func
        data_value *= p_elem
        count_mult += (newton_step[1] + 2)

    return prob, count_mult