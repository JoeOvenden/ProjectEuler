
def test(numerator, denominator):
    isExample = False
    numerator_list = list(str(numerator))
    denominator_list = list(str(denominator))
    value1 = numerator/denominator
    if int(denominator_list[1]) != 0 and numerator_list[1] == denominator_list[0]:
        value2 = int(numerator_list[0])/int(denominator_list[1])
    else:
        value2 = 10
    if numerator_list[0] == denominator_list[1]:
        value3 = int(numerator_list[1])/int(denominator_list[0])
    else:
        value3 = 10
    if value1 == value2 or value1 == value3:
        print(str(numerator)+"/"+str(denominator))
        print(value1, value2, value3)
        print()
        isExample = True
    return isExample

def Main():
    # I will make the assumption that no combinations like
    #    ab/cb = a/c can be found where b != 0
    # should be easy to prove
    numerator = 10
    denominator = 10
    isExample = False
    while numerator < 99:
        while denominator < 100:
            isExample = test(numerator, denominator)
            denominator += 1
        numerator += 1
        denominator = numerator + 1
                
                

if __name__ == "__main__":
    Main()
