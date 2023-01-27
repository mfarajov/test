import math

def add(x, y):
    """Add Function"""
    return x + y


def subtract(x, y):
    """Subtract Function"""
    return x - y


def multiply(x, y):
    """Multiply Function"""
    return x * y


def divide(x, y):
    """Divide Function"""
    if y == 0:
        raise ValueError('Can not divide by zero!')
    return x / y

# adding power function
def power(x, y):
    """Power function"""
    return x**y


# adding square root function
def square_root(x):
    """Square Root Function"""
    return math.sqrt(x)