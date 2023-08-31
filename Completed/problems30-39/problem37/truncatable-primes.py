#Project Euler Problem 37 - Truncatable primes

from math import ceil, sqrt

class Problem:
    def __init__(self):
        self.primes = []
        self.get_more_primes()
        self.Main()

    def get_more_primes(self):
        if self.primes == []:
            self.maximum_prime_value = 10000
            self.primes = get_primes(self.maximum_prime_value)
        else:
            self.maximum_prime_value *= 10
            new_primes = get_primes(self.maximum_prime_value,self.primes)
            self.primes = new_primes
        self.prime_list_length = len(self.primes)
        print("Primes generated up to:",self.maximum_prime_value)

    def isPrime(self,p):
        if p in self.primes:
            return True
        else:
            return False
            

    def check_truncatable_prime(self,p):
        #left to right
        truncatable = True
        if not p < 10:
            p = str(p)
            digits = len(p)
            p_altered_right = p
            p_altered_left = p
            for i in range(digits-1):
                #p_altered_right is for removing the digits from the right
                #p_altered_left is for removing the digits from the left
                p_altered_right = p_altered_right[:-1]
                p_altered_left = p_altered_left[1:digits]
                if self.isPrime(int(p_altered_right)) is False or self.isPrime(int(p_altered_left)) is False:
                    truncatable = False                
        else:
            truncatable = False

        return truncatable

    def Main(self):
        total = 0
        i = 0
        n_primes_found = 0
        finished = False
        while not finished:
            p = self.primes[i]
            isTruncatable = self.check_truncatable_prime(p)
            if isTruncatable:
                total += p
                n_primes_found += 1
                print(p,n_primes_found)
                if n_primes_found == 11:
                    finished = True
            i += 1
            if i == self.prime_list_length:
                self.get_more_primes()
        print("Total:",total)

def get_primes(n, prime_list = [2, 3]):
    #generates a list of all primes <= n and >= start
    primes = prime_list
    a = primes[len(primes)-1]+2
    while a <= n:
        isPrime = True
        for i in range(2,ceil(sqrt(a)) + 1):
            if a % i == 0:
                isPrime = False
                break
        if isPrime:
            primes.append(a)
        a += 2
    return primes    

def Main():
    P = Problem()

if __name__ == "__main__":
    Main()
