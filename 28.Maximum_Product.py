# Write a program to find the maximum product of two integers in an array.


def max_product(array):
    n = len(array)
    if n < 2:
        return "Not enough elements for a pair"

    max_prod = array[0] * array[1]

    for i in range(n):
        for j in range(i + 1, n):
            product = array[i] * array[j]
            if product > max_prod:
                max_prod = product

    return max_prod


array = list(map(int, input("Enter the numbers for array: ").split()))
print(f"Maximum Product In The Array Is: {max_product(array)}")
