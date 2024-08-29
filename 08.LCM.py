# Write a function to find the least common multiple (LCM) of two numbers.


def gcd(a, b):
    while b != 0:
        remainder = a % b
        a = b
        b = remainder
    return a


def lcm(a, b):
    gcd_value = gcd(a, b)
    return (a * b) // gcd_value


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

result = lcm(a, b)
print(f"The LCM of {a} & {b} is {result}.")
