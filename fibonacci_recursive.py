# recursion in this case is very inefficient for numbers greater than 30


def get_fibonacci(n):
    if n > 1:
        return get_fibonacci(n-1) + get_fibonacci(n-2)
    return n


def sum_fibonacci(n):
    if n < 1:
        return 0
    return sum_fibonacci(n-1) + get_fibonacci(n)


def ratio_fibonacci(n):
    if n == 1:
        return 1
    return get_fibonacci(n)/get_fibonacci(n-1)
