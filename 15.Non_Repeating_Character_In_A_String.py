# Write a program to find the first non-repeating character in a string.

def nonrepeating_character(string):
    char_count = {}

    for char in string:
        if char in char_count:
            char_count[char] +=1
        else:
            char_count[char] =1

    for char in string:
        if char_count[char]==1:
            return char
    return None

string = input("Enter a string: ")
print("The first Non-Repeating character in a string is:",nonrepeating_character(string))