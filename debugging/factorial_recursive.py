#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculates the factorial of a non-negative integer using recursion.

    Parameters:
        n (int): A non-negative integer for which the factorial is to be calculated.

    Returns:
        int: The factorial of the input number n.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Read the number from the command-line argument
f = factorial(int(sys.argv[1]))

# Print the factorial result
print(f)
