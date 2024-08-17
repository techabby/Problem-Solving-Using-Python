def find_missing(n, array):

    expected_sum = n * (n + 1) // 2
    actual_sum = sum(array)
    missing_number = expected_sum - actual_sum

    return missing_number


n = int(input("Enter the value of n (The Range): "))
array = list(map(int, input(f"Enter {n-1} numbers seprated by spaces: ").split()))

print("The missing number in the array is:", find_missing(n, array))
