# o(2n)^2 -> o(n)^2 
from typing import List


def numEnclaves(grid: List[List[int]]) -> int:
    count = 0
    exited = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                if (i + 1) == len(grid) or i == 0 and (j + 1) == len(grid[0]) or j == 0:
                    exited.append((i, j))
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1 and exited.count((i, j)) == 0:
                if exited.count((i+1, j)) == 1 or\
                        exited.count((i-1, j)) == 1 or\
                        exited.count((i, j+1)) == 1 or\
                        exited.count((i, j-1)) == 1:
                    exited.append((i, j))
                else:
                    count += 1
    return count


grid = [[0, 1, 1, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 0]]
grid_1 = [[0, 0, 0, 0], [1, 0, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]
print(numEnclaves(grid_1))
