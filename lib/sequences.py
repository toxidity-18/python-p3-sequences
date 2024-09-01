#!/usr/bin/env python3
def print_fibonacci(n):
    # Handle edge case for n <= 0
    if n <= 0:
        print([])
        return

    # Initialize the Fibonacci sequence list
    fib_sequence = [0, 1]
    
    # Generate the Fibonacci sequence up to length n
    while len(fib_sequence) < n:
        next_fib = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_fib)
    
    # Print the Fibonacci sequence list
    print(fib_sequence[:n])
