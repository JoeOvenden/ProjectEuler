# Jonathan Ovenden 15/06/2023
# Project Euler Problem 55
# https://projecteuler.net/problem=55

from time import time

def is_palindrome(n):
    n_reversed = int(str(n)[::-1])
    if n == n_reversed:
        return True


def is_lychrel(n):
    # as per Problem 55's description, assume lychrel is true and test the first
    # 50 iterations to see if it is false
    lychrel = True
    for i in range(50):
        n_reversed = int(str(n)[::-1])
        n += n_reversed
        if is_palindrome(n):
            lychrel = False
            break
    return lychrel


def main():
    # counts how many lychrel numbers there are below 10,000
    counter = 0
    for n in range(10000):
        if is_lychrel(n):
            counter += 1
    print("Answer: there are", counter, "lychrel numbers below 10 thousand.")


if __name__ == "__main__":
    start_time = time()
    main()
    print("Time taken:", time() - start_time)