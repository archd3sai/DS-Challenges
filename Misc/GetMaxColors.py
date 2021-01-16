from itertools import combinations

def getMaxColors(prices, money):
    prices_sum = []
    for i in reversed(range(1, len(prices)+1)):
        comb = [sum(j) for j in list(combinations(prices, i))]
        for k in comb:
            if k <= money:
                return i
    return 0

getMaxColors([1, 1, 2, 1], 4)
