#Project Euler Problem 36 - Double-base palindromes

from copy import deepcopy

class BinaryNumber:
    def __init__(self,bits):
        #only built for itterating from 00000 to 11111, (e.g. if bits = 5)
        #suppose bits = 5, binary_list is set to [0,0,0,0,0]
        self.bits = bits
        self.decimal = 0
        self.binary_list = self.generate_list()

    def add_1(self):
        i = self.bits - 1
        self.binary_list[i] += 1
        valid = False
        while not valid:
            if self.binary_list[i] == 2:
                if i == 0:
                    valid = True
                    self.increase_bits()
                else:
                    self.binary_list[i] = 0
                    i -= 1
                    self.binary_list[i] += 1
            else:
                valid = True
        self.decimal += 1

    def increase_bits(self):
        self.bits += 1
        self.binary_list = self.generate_list()
        self.binary_list[0] = 1

    def generate_list(self):
        binary_list = []
        for i in range(self.bits):
            binary_list.append(0)
        return binary_list

    def display(self):
        print()
        print(self.binary_list)
        print("Decimal:",self.decimal)
        print()

    def check_palindrome(self):
        #note a more efficient way would be just to compare 0 with n
        #1 with n-1, 2 with n-2 etc, (index)
        reverse_binary_list = deepcopy(self.binary_list)
        reverse_binary_list.reverse()
        if reverse_binary_list == self.binary_list:
            return True
        else:
            return False

def check_palindrome_decimal(decimal):
    decimal_string = str(decimal)
    decimal_backwards = decimal_string[::-1]
    if decimal_backwards == decimal_string:
        return True
    else:
        return False

def Main():
    total = 0
    binary_number = BinaryNumber(1)
    for i in range(1000000):
        isPalindrome_binary = binary_number.check_palindrome()
        isPalindrome_decimal = check_palindrome_decimal(binary_number.decimal)
        if isPalindrome_binary and isPalindrome_decimal:
            total += binary_number.decimal
            binary_number.display()
        binary_number.add_1()
    print(total)

if __name__ == "__main__":
    Main()
