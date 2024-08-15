# Write a program to compress a string using the counts of repeated characters.


def compressing_string(string):
    if not string:
        return ""

    compressed = []
    count = 1

    for i in range(1, len(string)):
        if string[i] == string[i - 1]:
            count += 1
        else:
            compressed.append(
                string[i - 1] + str(count) if count > 1 else string[i - 1]
            )
            count = 1

    compressed.append(string[-1] + str(count) if count > 1 else string[-1])

    return "".join(compressed)


string = input("Enter a string: ")
print(compressing_string(string))
