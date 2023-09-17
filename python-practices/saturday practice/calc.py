import sys

def calculate_expression(expression):
    try:
        result = eval(expression)
        print(f"Result: {result}")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python calculator.py <math_expression>")
    else:
        math_expression = sys.argv[1]
        calculate_expression('a+b')
