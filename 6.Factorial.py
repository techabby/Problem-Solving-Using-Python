# Write a program to find the factorial of a number.


num = int(input("Enter a number: "))
factorial = 1

for i in range(num, 0, -1):
    factorial = factorial * i

print(f"\nThe factorial of {num} is {factorial}.")
