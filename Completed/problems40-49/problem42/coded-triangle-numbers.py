# Jonathan Ovenden
# Project Euler Problem 42 - Coded Triangle Numbers
# https://projecteuler.net/problem=42

import sys, os
sys.path.append(os.path.abspath(r"..\..\..\helpers"))
from helpers import get_triangle_numbers

class Problem():
    def __init__(self):
        self.main()

    def main(self):
        word_file = open("words.txt",'r')
        word_file_lines = word_file.readlines()
        words = word_file_lines[0].split(",")

        # 5000 is chosen as it seems to be suitably big enough so that
        # any word value does not exceed it
        triangle_numbers = get_triangle_numbers(5000)
        amount_of_t_words = 0
        for word in words:
            # remove " from beginning and end of word
            word = word[1:-1]
            if get_word_value(word) in triangle_numbers:
                amount_of_t_words += 1
        print(amount_of_t_words)
        

def get_word_value(word):
    # maps each letter to its order in the alphabet and sums to get word value
    # a = 1, b = 2, ...
    value = 0
    letter_list = list(word)
    for letter in letter_list:
        value += ord(letter.upper()) - 64
    return value


if __name__ == "__main__":
    P = Problem()

    
