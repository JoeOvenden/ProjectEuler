# Jonathan Ovenden 13/06/2023
# Project Euler Problem 35 - Circular Primes
# https://projecteuler.net/problem=35

import sys, os
sys.path.append(os.path.abspath(r"..\..\..\helpers"))
from helpers import get_primes_up_to, binary_search, get_unique_cycles
from bisect import insort
from time import time

def main():
    primes = get_primes_up_to(999999)
    processed_primes = []
    n = 0
    for p in primes:
        if binary_search(processed_primes, p) is False:
            cycles = get_unique_cycles(p)
            isCircular = True
            for cycle in cycles:
                if binary_search(primes, cycle) is False:
                    isCircular = False
                else:
                    insort(processed_primes, cycle)
            if isCircular:
                n += len(cycles)
    print(n)


if __name__ == "__main__":
    start_time = time()
    main()
    print("Time taken:", time() - start_time)