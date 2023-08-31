# Jonathan Ovenden 14/06/2023
# Project Euler Problem 45 - Triangular, Pentagonal, and Hexagonal
# https://projecteuler.net/problem=45

from time import time
import sys, os
sys.path.append(os.path.abspath(r"..\..\..\helpers"))
from helpers import get_N_triangle_numbers, get_N_pentagon_numbers, binary_search


def main():
    # According to wikipedia every hexagonal number is a triangular number, but
    # only every other triangle number is a hexagonal number, starting with the 1st
    # We will therefore go through the evenly indexed triangular numbers and check
    # If they are pentagonal numbers
    # 500000 was chosen because it was big enough to get the required result
    # and runtime was still just 1.6 seconds

    triangle_numbers = get_N_triangle_numbers(500000)
    pentagon_numbers = get_N_pentagon_numbers(500000)
    for i in range(0, len(triangle_numbers), 2):
        triangle_number = triangle_numbers[i]
        if binary_search(pentagon_numbers, triangle_number):
            print(triangle_number)
            

if __name__ == "__main__":
    start_time = time()
    main()
    print("Time taken:", time() - start_time)