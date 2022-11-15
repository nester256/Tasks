from typing import List
# Сложность O(n^2)
def getDescentPeriods(prices: List[int]) -> int:
    result = len(prices)
    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            if prices[i] - prices[j] == 1:
                result += 1
                if prices[i] - prices[j] and prices[j] - prices[j + 1] == 1:
                    result += 1
    return result


print(getDescentPeriods([3, 2, 1, 4]))
