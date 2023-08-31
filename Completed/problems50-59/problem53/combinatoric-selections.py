# Jonathan Ovenden 15/06/2023
# Project Euler Problem 53 - Combinatoric Selections
# https://projecteuler.net/problem=53

import sys, os
sys.path.append(os.path.abspath(r"..\..\..\helpers"))
from helpers import binary_search
from math import factorial
from time import time

# factorial(i) is found at FACTORIALS
FACTORIALS = []
N = 100
for i in range(N + 1):
    FACTORIALS.append(factorial(i))


def n_choose_r(n, r):
    # r must be less than or equal to n
    return FACTORIALS[n]/(FACTORIALS[r] * FACTORIALS[n - r])


def main():
    # We know from the problem description that we first get values of 1 million
    # when n = 23, so we start there.
    # For each value of n, r can take values 0 to n, so we loop through r values as such
    counter = 0
    for n in range(23, N + 1):
        for r in range(n):
            if n_choose_r(n, r) > 1000000:
                counter += 1
    print("Answer:", counter)


if __name__ == "__main__":
    start_time = time()
    main()
    print("Time taken:", time() - start_time)