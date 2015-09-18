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
