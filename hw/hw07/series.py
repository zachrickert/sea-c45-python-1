def fibonacci(n):
    """
    Return the nth number from the fibonacci sequence

    Example:    fibonacci(0) == 0
                fibonacci(1) == 1
                fibonacci(n) == fibonacci(n-1) + fibonacci(n-2)

    """

    if (n == 0):
        x = 0
    elif (n == 1):
        x = 1
    else:
        x = fibonacci(n - 1) + fibonacci(n - 2)

    return x


def lucas(n):
    """
    Return the nth number from the lucas sequence

    Example:    lucas(0) == 2
                lucas(1) == 1
                lucas(n) == lucas(n-1) + lucas(n-2)

    """

    if (n == 0):
        x = 2
    elif (n == 1):
        x = 1
    else:
        x = lucas(n - 1) + lucas(n - 2)

    return x


def sum_series(n, n0, n1):
    """
    Return the nth number from a sum sequence

    Example:    sum_series(0, n0, n1) == n0
                sum_series(1, n0, n1) == n1
                sum_series(n, n0, n1) ==
                    sum_series(n-1, n0, n1) + sum_series(n-2, n0, n1)

    """

    if (n == 0):
        x = n0
    elif (n == 1):
        x = n1
    else:
        x = sum_series(n - 1, n0, n1) + sum_series(n - 2, n0, n1)

    return x
