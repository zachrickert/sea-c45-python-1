def fibonacci(n):
    """
    Return the nth number from the fibonacci sequence

    Example:    fibonacci(0) == 0
                fibonacci(1) == 1

    """

    if (n == 0):
        x = 0
    elif (n == 1):
        x = 1
    else:
        x = fibonacci(n - 1) + fibonacci(n - 2)

    return x
