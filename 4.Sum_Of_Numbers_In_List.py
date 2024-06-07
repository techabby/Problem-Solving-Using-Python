# Write a program to sum all the numbers in a list.

i = int(input("Enter number of numbers you want to add in the list: \n"))
list = []

for j in range(i):
    no = int(input("Emter a number: "))
    list.append(no)

sum = 0

for num in list:
    sum = sum + num

print(f"\nThe sum of {i} numbers is {sum}.")
