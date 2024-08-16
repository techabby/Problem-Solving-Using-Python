# Write a program to find all permutations of a string.


def permutation(string, left, right):

    if left == right:
        print("".join(string))
    else:
        for i in range(left, right + 1):

            string[left], string[i] = string[i], string[left]
            permutation(string, left + 1, right)
            string[left], string[i] = string[i], string[left]


def finding_permutation(string):
    permutation(list(string), 0, len(string) - 1)


string = input("Enter a string: ")
print("\nThe permutations of given string are: ")
finding_permutation(string)
