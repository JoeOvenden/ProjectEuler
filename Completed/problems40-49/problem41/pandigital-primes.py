# Jonathan Ovenden 13/06/2023
# Project Euler Problem 41 - Pandigital Primes
# https://projecteuler.net/problem=41

import sys, os
sys.path.append(os.path.abspath(r"..\..\..\helpers"))
from helpers import get_primes_up_to
from math import log, sqrt, trunc
from itertools import permutations

def is_prime(number):
    isPrime = True
    divisor_limit = trunc(sqrt(number))
    for divisor in PRIMES:
        if divisor > divisor_limit:
            break
        else:
            if number % divisor == 0:
                isPrime = False
                break
    if isPrime:
        return True
    else:
        return False


def main():
    # Pandigital numbers are the permutations of the numbers 1 to n so we use
    # lib itertools to generate exactly that. 
    # Then if the number is also prime we have a pandigital prime
    largest_panprime = 2143
    digits = "123"
    for i in range(4, 9):
        digits += str(i)
        digit_permutations = list(permutations(digits))
        for p in digit_permutations:
            p = int(''.join(p))
            if is_prime(p) and p > largest_panprime:
                largest_panprime = p
    print(largest_panprime)


if __name__ == "__main__":
    PRIMES = get_primes_up_to(trunc(sqrt(987654321)))
    main()