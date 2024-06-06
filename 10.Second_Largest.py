# Write a function to find the second largest number in a list.

list = []

rang = int(input("Enter how many numbers do you want in the list?: "))
for i in range(rang):
    num = int(input("Enter a number: "))
    list.append(num)

list.sort(reverse=True)

sec_largest = list[1]

print("The second largest number in the list is ", sec_largest)
