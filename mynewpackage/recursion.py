def sum_array(array):

    '''Return sum of all items in array'''
    sum_of = 0

    for i in array:
        if isinstance(i, int):
            sum_of += i
        elif isinstance(i, list):
            sum_of += sum_array(i)
    return sum_of


def fibonacci(n):

    '''Return nth term in fibonacci sequence'''
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def factorial(n):

    '''Return n!'''
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)


def reverse(word):

    '''Return word in reverse'''
