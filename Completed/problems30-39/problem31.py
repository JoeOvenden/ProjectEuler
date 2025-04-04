coins = [0, 0, 0, 0, 0, 0, 0, 0]
values = [1, 2, 5, 10, 20, 50, 100, 200]
solved = False
n = 0

def addCoin(i):
    global n, coins
    coins[i] += 1
    coinSum = calcSum()
    if coinSum == 200:
        n += 1
        print(coins)
    return coinSum

def calcSum():
    global coins
    return sum([coins[k] * values[k] for k in range(8)])

def reset(i):
    for j in range(i + 1):
        coins[j] = 0 

def main():
    global solved
    index = 0
    while not solved:
        coinSum = addCoin(index)
        if coinSum >= 200:
            while coinSum >= 200:
                reset(index)
                index += 1
                if index == 8:
                    solved = True
                    break
                coinSum = addCoin(index)
            index = 0

if __name__ == "__main__":
    main()
    print(n)
