# Write a program to find the intersection of two lists.

list1 = [32, 23, 2, 4, 1, 31, 35, 21, 769, 78, 5]
list2 = [23, 35, 7, 32, 5, 6, 8, 4, 34, 56, 3, 51]
list3 = []

for i in list1:
    for j in list2:
        if i == j:
            list3.append(i)

print("The intersection of two lists is:", list3)
