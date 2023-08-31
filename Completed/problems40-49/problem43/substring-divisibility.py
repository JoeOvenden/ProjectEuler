# Jonathan Ovenden 14/06/2023
# Project Euler Problem 43 - Sub-string Divisibility
# https://projecteuler.net/problem=43

from itertools import permutations
from time import time


def main():
    # generate all 0 to 9 pandigitals
    # first check divisbility by 2 and then make sure no leading zero as this
    # check divisibility by 2 and 5 first as it is cheap and removes a large
    # amount of possible numbers. Then proceed with rest of checks.
    pandigitals = permutations('1234567890')
    total = 0
    for pandigital in pandigitals:
        pandigital = ''.join(list(pandigital))
        if pandigital[3] in ['2', '4', '6', '8', '0']:
            if pandigital[5] in ['0', '5']:
                if pandigital[0] != '0':
                    if int(pandigital[2:5]) % 3 == 0:
                        if int(pandigital[4:7]) % 7 == 0:
                            if int(pandigital[5:8]) % 11 == 0:
                                if int(pandigital[6:9]) % 13 == 0:
                                    if int(pandigital[7:10]) % 17 == 0:
                                        total += int(pandigital)
    print(total)

if __name__ == "__main__":
    start_time = time()
    main()
    print("Time taken:", time() - start_time)