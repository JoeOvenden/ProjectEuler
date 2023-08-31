# Jonathan Ovenden 13/06/2023
# Project Euler Problem 52 - Permuted Multiples
# https://projecteuler.net/problem=52


def main():
    x = 142857
    """ 
    I actually happened to know the answer to this one already
    This is because when I was young my dad told me about an interesting property
    about the number 7:
    If you take any integer (thats not divisible by 7) and divide it by 7, 
    the decimal part of the number will be a recurring decimal of order 6 that
    is made up of 142857 but starting in a different place depending on the numerator
    
    1/7 = 0.142857142857...
    2/7 = 0.285714285728...
    3/7 = 0.428571428571..
    etc.
    Pretty cool if you ask me!
    """
    
    for i in range(1, 7):
        print(x * i)

if __name__ == "__main__":
    main()