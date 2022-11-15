from typing import List
# Сложность O(n^2)

def maxScoreSightseeingPair(values: List[int]) -> int:
    max_value = 0
    for i in range(len(values)):
        for j in range(i + 1, len(values)):
            value = values[i] + values[j] + i - j
            max_value = value if max_value < value else max_value
    return max_value


print(maxScoreSightseeingPair([8, 1, 5, 2, 6]))
