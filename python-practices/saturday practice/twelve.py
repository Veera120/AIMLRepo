import sys

# Check if the correct number of command-line arguments is provided
if len(sys.argv) != 2:
    print("Usage: python calculator.py <math_expression>")
    sys.exit(1)

# Get the mathematical expression from the command line
math_expression = sys.argv[1]

try:
    # Evaluate the mathematical expression
    result = eval(math_expression)
    print("Result:", result)
except Exception as e:
    print("Error:", e)

#python calculator1.py "2 + 3 * 5"