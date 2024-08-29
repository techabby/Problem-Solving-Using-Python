# Write a function to check if a string is a palindrome.

string = input("Enter a string: ")

rvr_string = string[::-1]

if string == rvr_string:
    print(f"\nThe string '{string}' is a palindrome.")
    print(f"This is the reversed string {rvr_string}.")
else:
    print(f"\nThe string '{string}' is a normal string.")
    print(f"This is the reversed string {rvr_string}.")
