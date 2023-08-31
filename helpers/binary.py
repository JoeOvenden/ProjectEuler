class BinaryNumber:
    def __init__(self,bits):
        #only built for itterating from 00000 to 11111, (e.g. if bits = 5)
        #suppose bits = 5, binary_list is set to [0,0,0,0,0]
        self.bits = bits
        self.decimal = 0
        self.binary_list = self.generate_list()
        self.overflow = False


    def count_ones(self):
        ones = 0
        for bit in self.binary_list:
            if bit == 1:
                ones += 1
        return ones


    def reset(self):
        for bit in self.binary_list:
            bit = 0


    def add_1(self):
        i = self.bits - 1
        self.binary_list[i] += 1
        valid = False
        while not valid:
            if self.binary_list[i] == 2:
                if i == 0:
                    valid = True
                    self.overflow = True
                else:
                    self.binary_list[i] = 0
                    i -= 1
                    self.binary_list[i] += 1
            else:
                valid = True
        self.decimal += 1
        return self.overflow


    def generate_list(self):
        binary_list = []
        for i in range(self.bits):
            binary_list.append(0)
        return binary_list

    
    def get_list(self):
        return self.binary_list


    def display(self):
        print()
        print(self.binary_list)
        print("Decimal:",self.decimal)
        print()
