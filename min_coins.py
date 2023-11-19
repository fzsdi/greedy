# Find minimum number of coins using greedy algorithm

def getCoins():
    inputString = input("Enter list of coins separated by space: ")
    coinList = inputString.split()
    for i in range(0, len(coinList)):
        coinList[i] = int(coinList[i])
    coinList.sort()
    inputString = input("Enter the coin you want to change: ")
    coin = int(inputString)
    return coinList, coin

coinList, coin = getCoins()
length = len(coinList)
length = length - 1
changeList = []

while length >= 0:
    c = coinList[length]
    while (coin >= c):
        coin = coin - c
        changeList.append(c)
    length = length - 1

print("The changed coins are: ", changeList, "\n"
      "And the minimum number of coins to create the coin is: ", len(changeList))