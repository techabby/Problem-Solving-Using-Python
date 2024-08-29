# Write a program to rotate a list by k elements.


def rotate(lst, k):
    k = k % len(lst)
    return lst[-k:] + lst[:-k]


org_list = [3, 4, 2, 5, 1, 6, 9, 7, 0, 8]
k = int(input("Enter value for k: "))

rotated_list = rotate(org_list, k)
print("Orignal List:", org_list)
print("Rotated List:", rotated_list)
