# Jonathan Ovenden
# Project Euler Problem 50 - Consecutive Prime Sums
# https://projecteuler.net/problem=50

import sys, os
sys.path.append(os.path.abspath(r"..\..\..\helpers"))
from helpers import binary_search, get_primes_up_to
from math import sqrt, trunc

def main():
    # for every prime number less than 1 million we analyse all the consecutive 
    # prime sums that begin with that prime
    # i.e. for p = 2, we have the sums, 
    # s1 = 2, 
    # s2 = 2 + 3, 
    # s3 = 2 + 3 + 5
    # up until the sum goes above 1 million

    consecutive_psum_max = 0
    total_max = 0
    p_max_index = 0
    p_index = 0
    for p_index in range(len(PRIMES)):
        consecutive_psum, total = get_longest_sum(p_index)
        if consecutive_psum > consecutive_psum_max:
            consecutive_psum_max = consecutive_psum
            total_max = total
            p_max_index = p_index

    print("The longest consecutive prime sum has", consecutive_psum_max, "summands")
    print("The sum total is", total_max)
    print("The first term is", PRIMES[p_max_index])
    print("Therefore the answer to Problem 50 is", total_max)


def get_longest_sum(p_index):
    # consecutive_psum_max keeps track of the longest consecutive prime sum that
    # meets the criteria.
    # total_max is the corresponding total of that sum
    total_max = PRIMES[p_index]
    consecutive_psum_max = 1

    # total is the running total of the prime sum
    # n is the running length of the prime sum

    total = total_max
    keepGoing = True
    n = 1
    while keepGoing:
        n += 1
        p_index += 1
        try:
            total += PRIMES[p_index]
        except IndexError:
            break

        if total > N:
            keepGoing = False

        else:
            if binary_search(PRIMES, total):
                consecutive_psum_max = n
                total_max = total

    return consecutive_psum_max, total_max


if __name__ == "__main__":
    N = 1000000
    PRIMES = get_primes_up_to(N)
    main()