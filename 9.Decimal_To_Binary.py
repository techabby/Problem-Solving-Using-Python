# Write a function to convert a decimal number to binary.

def DTB(n):
    if n == 0:
        return "0"

    binary = ""
    while n > 0:
        remainder = n % 2
        n = n // 2
        binary = (
            str(remainder) + binary
        )  

    return binary

n = int(input("Enter a number: "))
result = DTB(n)

print(f"The binary code for {n} is {result}.") 