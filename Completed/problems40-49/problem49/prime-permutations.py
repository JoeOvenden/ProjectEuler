# Jonathan Ovenden 14/06/2023
# Project Euler Problem 49 - Prime Permutations
# https://projecteuler.net/problem=49

import sys, os
sys.path.append(os.path.abspath(r"..\..\..\helpers"))
from helpers import get_primes_up_to, binary_search
from time import time

def are_permutations(number1, number2):
    # checks to see if number1 and number2 are permutations of each other
    number1_digits = list(str(number1))
    number1_digits.sort()
    number2_digits = list(str(number2))
    number2_digits.sort()
    if number1_digits == number2_digits:
        return True
    else:
        return False


def main():
    # loop through the 4 digit primes
    # check first that adding 3330 results in primes
    # then check if they are permutations of each other
    primes = get_primes_up_to(9999)
    found = False

    # primes[168] is the first prime above 1000
    index = 168
    while not found:
        term_1 = primes[index]
        term_2 = term_1 + 3330
        if binary_search(primes, term_2):
            term_3 = term_2 + 3330
            if binary_search(primes, term_3):
                if are_permutations(term_1, term_2):
                    if are_permutations(term_1, term_3):
                        if term_1 != 1487:
                            print("The other sequence is:", term_1, term_2, term_3)
                            print("Therefore the answer is:", str(term_1) + str(term_2) + str(term_3))
                            found = True
        index += 1


if __name__ == "__main__":
    start_time = time()
    main()
    print("Time taken:", time() - start_time)