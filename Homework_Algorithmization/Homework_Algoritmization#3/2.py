# o(3n)^2 -> o(n)^2
from typing import List


def closedIsland(self, grid: List[List[int]]) -> int:
    res = 0

    def dfs(i, j):
        if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] != 1:
            grid[i][j] = 1
            dfs(i, j - 1)
            dfs(i, j + 1)
            dfs(i - 1, j)
            dfs(i + 1, j)

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if i == 0 or\
                j == 0 or\
                    i == len(grid) - 1 or\
                    j == len(grid[0]) - 1:
                dfs(i, j)

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                dfs(i, j)
                res += 1

    return res
