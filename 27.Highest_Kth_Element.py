# Write a program to find the k-th largest element in an array.

list_array = list(
    map(int, input(f"Enter the nuumbers you want to add in an array: ").split())
)

set_array = set(list_array)
array = list(set_array)
array.sort(reverse=True)

kth_value = int(
    input(f"Enter the number for k (should be less than or equal to {len(array)}): ")
)

if kth_value <= 0 or kth_value > len(array):
    print("Invalid value for K")
else:
    highest_kth_element = array[kth_value - 1]
    print("The kth highest element in the given array is:", highest_kth_element)
