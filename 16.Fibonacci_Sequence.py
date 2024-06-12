# Write a program to generate the Fibonacci sequence up to n term


def fibonacci(n):
    
    if n == 0:
        return []
    elif n == 1:
        return [0]

    sequence = [0, 1]

    for i in range(2, n):
        next_fib = sequence[-1] + sequence[-2]
        sequence.append(next_fib)

    return sequence


n = int(input("Enter the value of n: "))

print(f"Fibonacci sequence up to {n} terms:")
print(fibonacci(n))
