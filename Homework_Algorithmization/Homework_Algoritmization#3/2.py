# o(3n)^2 -> o(n)^2
from typing import List


def closedIsland(self, grid: List[List[int]]) -> int:
    res = 0                             # счётчик количества закрытых островов

    def dfs(i, j):                      # метод с помощью рекурсии идёт по всем соседним клеточкам земли и делает их водой
        if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] != 1:
            grid[i][j] = 1
            dfs(i, j - 1)
            dfs(i, j + 1)
            dfs(i - 1, j)
            dfs(i + 1, j)

    for i in range(len(grid)):
        for j in range(len(grid[0])):   # цикл по всем крайним клеточкам и делает их водой если они являются землёй
            if i == 0 or\
                j == 0 or\
                    i == len(grid) - 1 or\
                    j == len(grid[0]) - 1:
                dfs(i, j)

    for i in range(len(grid)):
        for j in range(len(grid[0])):   # цикл по клеточкам земли оставшимся после предыдущих изменений
            if grid[i][j] == 0:
                dfs(i, j)               # преврящает её и её соседей что бы не посчитать ещё раз
                res += 1                # увеличивает счётчик

    return res                          # возвращает счётчик
