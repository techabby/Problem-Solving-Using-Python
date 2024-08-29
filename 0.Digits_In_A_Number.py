# Write a program to count the number of digits in a number.

number = input("Enter a number: ")

number = str(number).replace("-", "").replace(".", "")

total_digits = 0
for digits in number:
    total_digits = total_digits + 1

print(total_digits)
