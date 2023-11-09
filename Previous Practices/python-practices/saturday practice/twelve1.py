def add(x, y):
    """Return the result of addition."""
    return x + y

def subtract(x, y):
    """Return the result of subtraction."""
    return x - y

def multiply(x, y):
    """Return the result of multiplication."""
    return x * y

def divide(x, y):
    """Return the result of division."""
    if y == 0:
        raise ValueError("Division by zero is not allowed.")
    return x / y