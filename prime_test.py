"""
Problem:

    The function is_prime takes in an intger and tests
    whether it is prime or not. It should print either
    "Prime" or "Non-Prime".

Tests:

    >>> is_prime(1)
    Non-Prime
    >>> is_prime(2)
    Prime
    >>> is_prime(7)
    Prime
    >>> is_prime(24)
    Non-Prime
    >>> is_prime(123)
    Non-Prime
    >>> is_prime(137)
    Prime

Hint:

    Count the number of factors!
"""

# Use this to test your solution. Don't edit it!
import doctest
def run_tests():
    doctest.testmod(verbose=True)


# Edit this code
def is_prime(n):

    a = 0

    for i in range(2, n):
        if n % i == 0:
            a = 1

    if n == 1:
        print("Non-Prime")

    elif a == 1:
        print("Non-Prime")

    else:
        print("Prime")



    
