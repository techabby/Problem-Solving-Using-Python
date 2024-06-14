# Write a program to reverse the words in a string.

string = input("Enter a string: ")

words = string.split()

reversed_words = []

for word in words:
    rvrs = word[::-1]
    reversed_words.append(rvrs)

print(" ".join(reversed_words))
