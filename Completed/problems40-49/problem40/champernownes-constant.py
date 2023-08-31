#Project Euler Problem 40 - Champernowne's constant

class Problem():
    def __init__(self):
        self.main()

    def main(self):
        decimals_list = []
        list_length = 0
        integer = 1
        while list_length < 1000000:
            integer_str = str(integer)
            integer_list = list(integer_str)
            decimals_list += integer_list
            list_length += len(integer_list)
            integer += 1
        for n in range(0,7):
            index = 10**n
            print(decimals_list[index-1])

if __name__ == "__main__":
    P = Problem()
