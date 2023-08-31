# Jonathan Ovenden 14/06/2023
# Project Euler Problem 47 - Distinct Prime Factors
# https://projecteuler.net/problem=47

from time import time
from sympy.ntheory import factorint

def check_distinct(factors_list):
    # factors_list is a list containing the 4 dictionaries of prime factors
    # the dictionaires should all be checked to be of length 4 already
    # goes through factors and if finds a duplicate distinct is set to False
    distinct_factors = []
    distinct = True
    for i in range(4):
        for factor in factors_list[i]:
            factor_pair = [factor, factors_list[i][factor]]
            if factor_pair in distinct_factors:
                distinct = False
                break
            else:
                distinct_factors.append(factor_pair)
    return distinct
    

def main():
    # get prime factors and if there are not 4 factors, empty the factor_list
    # since it breaks the consecutive streak
    # once 4 consecutive numbers having 4 factors each have been found,check distinct.
    found = False
    number = 2
    N = 4
    factors_list = []
    while not found:
        factors = factorint(number)
        if len(factors) != N:
            factors_list = []
        else:
            factors_list.append(factors)

        if len(factors_list) == N:
            if check_distinct(factors_list):
                print("Answer is:", number - 3)
                found = True

        number += 1
        

if __name__ == "__main__":
    start_time = time()
    main()
    print("Time taken:", time() - start_time)