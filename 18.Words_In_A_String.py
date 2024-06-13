# Write a program to count the number of words in a string.


def words_counter(string):

    words = string.split()
    word_count = len(words)

    return word_count


string = input("Enter a string: ")
print("The number of words in give string is:", words_counter(string))
