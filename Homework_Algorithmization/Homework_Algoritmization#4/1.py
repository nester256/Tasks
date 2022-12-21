# O(n)
from typing import List


def findLongestChain(self, pairs: List[List[int]]) -> int:
    result = []
    for start, end in sorted(pairs):
        idx = bisect.bisect_left(result, start)
        if idx == len(result):
            result.append(end)
        else:
            result[idx] = min(result[idx], end)
    return len(result)