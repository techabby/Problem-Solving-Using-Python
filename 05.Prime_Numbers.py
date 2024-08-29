# Write a function to check if a number is prime.


def prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:  
            return False
    return True

num = int(input("Enter a number: "))  

if prime(num):
    print(f"The number {num} is a prime number.")
else:
    print(f"The number {num} is not a prime number.")

