def sum_even_fibonacci_terms(max_value):
    # Start the fibonacci sequence with 1 and 2
    fib = [1, 2]

    # Build the fibonacci sequence until the next value is not less than max
    next_val = fib[-1] + fib[-2]
    while next_val < max_value:
        fib.append(next_val)
        next_val = fib[-1] + fib[-2]

    # Return the sum of the even values in the sequence
    return sum([x for x in fib if x % 2 == 0])
