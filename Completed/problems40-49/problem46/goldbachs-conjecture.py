# Jonathan Ovenden 14/06/2023
# Project Euler Problem 46 - Goldbach's Other Conjecture
# https://projecteuler.net/problem=46

import sys, os
sys.path.append(os.path.abspath(r"..\..\..\helpers"))
from helpers import binary_search, get_N_primes, get_N_more_primes
from time import time


def check_conjecture(number, primes):
    i = 0
    # loops through primes
    # and for each prime loops through integers until the sum goes above number
    # then onto the next prime

    # primes[i] is the prime currently being tested
    # so if primes[i] >= number, then this means we haven't found a suitable sum
    # that fits goldbach's conjecture
    # and so the conjecture is disproven

    fits_conjecture = False
    while primes[i] < number and fits_conjecture is False:
        p = primes[i]
        n = 1
        too_large = False
        while not too_large:
            total = p + 2 * (n ** 2)
            if total > number:
                too_large = True
            elif total == number:
                fits_conjecture = True
                break
            n += 1
        # increment the index so that we can test the next prime
        i += 1
    return fits_conjecture


def main():
    # loop through odd numbers
    # first check to see if composite (i.e. not prime)
    # then if doesn't fit the goldbachs conjecture, output the number
    # and we have our solution
     
    found = False
    primes = get_N_primes(1000)
    largest_prime = primes[-1]
    number = 9
    while not found:
        if number > largest_prime:
            get_N_more_primes(primes, 100)
            largest_prime = primes[-1]
        if binary_search(primes, number) is False:
            if check_conjecture(number, primes) is False:
                print("The smallest number to disprove goldbach's conjecture is:", number)
                break
        number += 2
    

if __name__ == "__main__":
    start_time = time()
    main()
    print("Time taken:", time() - start_time)