# Write a function to reverse a string.

str = input("Enter any string: ")

rvrs = str[::-1]
print("The reverse of the string is ", rvrs)


# Also can be done using functions

str2 = input("\nEnter another string: ")

def reverse(str2):
    return str2[::-1]

func = reverse(str2)
print("The reverse of the string is ", func)
