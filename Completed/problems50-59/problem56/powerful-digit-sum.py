# Jonathan Ovenden 15/06/2023
# Project Euler Problem 56 - Powerful Digit Sum
# https://projecteuler.net/problem=56

from time import time

def get_digit_sum(number):
    total = 0
    for digit in str(number):
        total += int(digit)
    return total


def main():
    # loop through all combinations for a, b < 100 and get digit sum
    # prints the largest
    maximal_digit_sum = 0
    for a in range(100):
        for b in range(100):
            digit_sum = get_digit_sum(a ** b)
            if digit_sum > maximal_digit_sum:
                maximal_digit_sum = digit_sum
    print("Answer: the maximal digit sum is", maximal_digit_sum)
            


if __name__ == "__main__":
    start_time = time()
    main()
    print("Time taken:", time() - start_time)