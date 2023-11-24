#!/usr/bin/env python3

def print_fibonacci(length):
    fib_sequence = []
    
    if length >= 1:
        fib_sequence.append(0)
    if length >= 2:
        fib_sequence.append(1)
    for n in range(2, length):
        next_number = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_number)

    print(fib_sequence)