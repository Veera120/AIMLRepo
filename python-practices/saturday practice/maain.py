# main.py
import my_math

if __name__ == "__main__":
    num = 5

    # Calculate and print the factorial of num
    fact = my_math.factorial(num)
    print(f"Factorial of {num} is: {fact}")

    # Check and print if num is prime
    is_prime = my_math.is_prime(num)
    if is_prime:
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")
