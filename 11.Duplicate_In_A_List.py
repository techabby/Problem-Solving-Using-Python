# Write a Program to remove duplicates from a list.

i = int(input("Enter the number of elements to add in a list: "))

temp_list = []
for items in range(i):
    items = input("Enter the element: ")
    temp_list.append(items)

list = list(set(temp_list))
print("This is the list after removing all the duplictes from it:\n", list)
