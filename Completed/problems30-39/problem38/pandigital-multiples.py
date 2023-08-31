#Project Euler Problem 38 - Pandigital multiples

#finding largest 1 to 9 pandigital number that can be formed
#by x with (1, 2, ... , n), n > 1

class Problem():
    def __init__(self):
        self.main()

    def isPandigital_combination(self):
        digits = []
        for i in range(1,self.n+1):
            digits += list(str(self.x*i))
        howManyDigits = len(digits)
        if howManyDigits == 9:
            pandigital = isPandigital_list(digits)
            if pandigital:
                concatenated_product = convertStringList_toInt(digits)
                if concatenated_product > self.largest_pandigital:
                    self.largest_pandigital = concatenated_product
        else:
            pandigital = False
        return pandigital, howManyDigits

    def main(self):
        self.x = 1
        self.n = 2
        self.largest_pandigital = 0
        while self.n < 10:
            self.x += 1
            pandigital, howManyDigits = self.isPandigital_combination()
            if howManyDigits >= 10:
                self.n += 1
                self.x = 1
        print(self.largest_pandigital)
                
def isPandigital_list(number_list):
    pandigital = True
    digits_used = []
    for d in number_list:
        if d in digits_used or d == '0':
            #this means it is not pandigital as each digit is only used once
            pandigital = False
            break
        else:
            digits_used.append(d)
    return pandigital

def convertStringList_toInt(string_list):
    x = ""
    for s in string_list:
        x += s
    x = int(x)
    return x

if __name__ == "__main__":
    P = Problem()
