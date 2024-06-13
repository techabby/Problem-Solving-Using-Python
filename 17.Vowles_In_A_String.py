# Write a program to count the number of vowels in a string.

def vowels_counter(string):
    Vowels = ["a","e","i","o","u","A","E","I","O","U"]
    vowels = 0 
    for i in string:
        if i in Vowels:
            vowels = vowels + 1
    return vowels

string = input("Enter a string: ")
print("The number of vowels in the given string is:",vowels_counter(string))