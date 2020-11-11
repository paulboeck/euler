import math


def is_prime(number):
    # Prime numbers are > 1 and are whole numbers
    if number <= 1 or number % 1 > 0:
        return False
    # 2 is s prime number but will fail the logic below so just return True if number is 2
    if number == 2:
        return True

    # If we find any factors between 3 and the square root of the number, then the number is not prime
    limit = int(math.sqrt(number))
    counter = 2
    while counter <= limit:
        if number % counter == 0:
            return False
        counter += 1
    return True


def largest_prime_factor(number):
    counter = int(math.sqrt(number) // 1)
    print(counter)
    while counter > 0:
        if number % counter == 0 and is_prime(counter):
            return counter
        counter -= 1
