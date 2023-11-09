# calculator.py

def add(a, b):
    """Returns the sum of two numbers."""
    return a + b

def subtract(a, b):
    """Returns the difference between two numbers."""
    return a - b

def multiply(a, b):
    """Returns the product of two numbers."""
    return a * b

def divide(a, b):
    """
    Returns the result of dividing two numbers.
    Raises a ValueError if the second number is 0.
    """
    if b == 0:
        raise ValueError("Division by zero is not allowed.")
    return a / b
