# Write a program to check if a string has all unique characters.


def unique_character(string):
    char_set = set()
    
    for char in string:
        if char in char_set:
            return "This string doesn't contains all the unique characters."
        char_set.add(char)
    return "This string contains all the unique characters."


string = input("Enter a string: ")
print(unique_character(string))
