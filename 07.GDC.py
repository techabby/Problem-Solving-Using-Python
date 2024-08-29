# Write a function to find the greatest common divisor (GCD) of two numbers.


def gcd(a, b):
    while b != 0:
        remainder = a % b
        a = b
        b = remainder
    return a


a = int(input("Enter first number: "))
b = int(input("Enter seccond number: "))

result = gcd(a, b)
print(f"The GCD of {a} & {b} is {result}.")
