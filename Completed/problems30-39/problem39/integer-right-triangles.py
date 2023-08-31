#Project Euler Problem 39 - Integer right triangles

from math import ceil

class Problem():
    def __init__(self):
        self.main()

    def get_numberOfSolutions(self):
        number_of_solutions = 0
        c = 1
        finished = False
        while c <= ceil(self.p/2):
            a = 1
            b = self.p - c - a
            c += 1
            while a <= b:
                if a**2 + b**2 == c**2:
                    print("Solution:",a,b,c)
                    number_of_solutions += 1
                a += 1
                b = self.p - c - a
        return number_of_solutions
            
            

    def main(self):
        self.p = 1
        self.maximum_solutions = 0
        self.p_solutions_maximised = -1
        while self.p <= 1000:
            number_of_solutions = self.get_numberOfSolutions()
            if number_of_solutions > self.maximum_solutions:
                self.maximum_solutions = number_of_solutions
                self.p_solutions_maximised = self.p
            self.p +=1
        print(self.maximum_solutions, self.p_solutions_maximised)

        
if __name__ == "__main__":
    P = Problem()
