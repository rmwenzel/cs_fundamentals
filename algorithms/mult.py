"""Multiplication algorithms."""


def recmult(a, b):
    """Recursive multiplication.

    Parameters
    ----------
    a: int or float
        number to be multiplied
    b: int or float
        number to be multiplied

    Returns
    -------
    a*b: int or float
        product of a and b
    """
    # if a, b are single digit integers return the product
    if a // 10 == 0 and b // 10 == 0:
        return a * b

    # else recursive calls
    elif a // 10 == 0:
        return 10 * recmult(a, b // 10) + a * (b % 10)

    elif b // 10 == 0:
        return 10 * recmult(a // 10, b) + (a % 10) * b

    else:
        return (100 * recmult(a // 10, b // 10) +
                10 * (recmult(a % 10, b // 10) +
                recmult(a // 10, b % 10)) +
                (a % 10) + (b % 10))


def karatsuba(a, b, n):
    """Recursive Karatsuba multiplication.

    Assumes that the length of a and b are even and both of length
    n.

    Parameters
    ----------
    a: int or float
        number to be multiplied
    b: int or float
        number to be multiplied
    n: int
        length of a and b

    Returns
    -------
    a*b: int or float
        product of a and b
    """
    # rewrite a and b
    a_0 = a % (10**(n / 2))
    a_1 = a // (10**(n / 2))
    b_0 = b % (10**(n / 2))
    b_1 = b // (10**(n / 2))

    # recursively compute a*b
    return ((10**n) * karatsuba(a_1, b_1) +
            (10**(n / 2) * (karatsuba(a_1, b_0) + karatsuba(a_0, b_1))) +
            karatsuba(a_0, b_0))
