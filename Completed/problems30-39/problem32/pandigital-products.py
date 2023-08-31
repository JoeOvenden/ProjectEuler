#Project Euler 32 - Pangital products

from math import ceil

def test(a,b):
    panditial_product = None
    return panditial_product

def get_smallest_b(a):
    if a < 10:
        smallest_b = 1000
    else:
        smallest_b = 100
        
    return smallest_b

def check_pandigital(a,b,c):
    pandigital = True
    digits = []
    digitsInCalculation = list(str(a)) + list(str(b)) + list(str(c))
    for d in digitsInCalculation:
        if d in digits or d == '0':
            #this means it is not pandigital as each digit is only used once
            pandigital = False
            break
        else:
            digits.append(d)
    return pandigital

def check_increase_a(a,b,c):
    if len(str(a)) + len(str(b)) + len(str(c)) == 10:
        return True
    else:
        return False
    

def Main():
    a = 1
    exitLoop = False
    pandigital_products = []
    b = get_smallest_b(a)
    total = 0
    while not exitLoop:
        c = a * b
        if check_pandigital(a,b,c) is True:
            if not c in pandigital_products:
                pandigital_products.append(c)
                total += c
        b += 1
        if check_increase_a(a,b,c) is True:
            a += 1
            b = get_smallest_b(a)
            if a == 100:
                exitLoop = True
    print("total is",total)

if __name__ == "__main__":
    Main()
