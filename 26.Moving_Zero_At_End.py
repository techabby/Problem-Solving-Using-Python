# Write a program to move all zeros to the end of an array.


def moving_zeros(array):
    non_zero = [num for num in array if num != 0]
    zero_count = array.count(0)
    result = non_zero + [0] * zero_count

    return result


array = list(map(int, input("Enter the numbers you wanna add in an array: ").split()))
print(moving_zeros(array))
