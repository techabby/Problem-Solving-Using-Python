# Write a program to merge two sorted lists.

list1 = [5, 23, 2, 131, 21, 32, 4]
list2 = [0, 234, 32, 7, 84, 989]

list1.sort()
list2.sort()

merged_list = list1 + list2

print("The merged list is:", merged_list)
