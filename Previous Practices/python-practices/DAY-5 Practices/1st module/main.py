# main.py

# Import built-in modules
import math

# Import custom modules
from my_math import add, subtract
from custom_module import CustomClass

# Use built-in modules
print(math.sqrt(25))

# Use custom modules
result_add = add(10, 5)
result_sub = subtract(10, 5)
print(f"Custom Addition: {result_add}")
print(f"Custom Subtraction: {result_sub}")

# Use custom class from custom_module
obj = CustomClass()
obj.say_hello()

# Handling errors for missing modules
try:
    import non_existent_module
except ImportError as e:
    print(f"Error: {e}")
