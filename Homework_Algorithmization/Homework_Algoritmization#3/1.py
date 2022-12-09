# o(2n)^2 -> o(n)^2 
from typing import List


def numEnclaves(grid: List[List[int]]) -> int:
    count = 0                           # Количество клеток котрые не выходят за край
    exited = []                         # Сюда буду записывать координаты тех клеток кторые выходят
    for i in range(len(grid)):
        for j in range(len(grid[0])):   # цикл по всем клеткам
            if grid[i][j] == 1:         # если клетка равна единице
                if (i + 1) == len(grid) or i == 0 and (j + 1) == len(grid[0]) or j == 0: # условике на поиск райних клеток земли
                    exited.append((i, j))
    for i in range(len(grid)):
        for j in range(len(grid[0])):                           # цикл по всем клеткам
            if grid[i][j] == 1 and exited.count((i, j)) == 0:   # Если клетки нет в списке и огна земля
                if exited.count((i+1, j)) == 1 or\
                        exited.count((i-1, j)) == 1 or\
                        exited.count((i, j+1)) == 1 or\
                        exited.count((i, j-1)) == 1:            # проверяем не содержатся ли её соседи в списке
                    exited.append((i, j))                       # Если содержится добавялем её в список тех выходящих
                else:
                    count += 1                                  # Увеличиваем счётчик если она не соответствует всем верхним условиям
    return count                                                # Возвращаем количество клеток которые не выходят за край


grid = [[0, 1, 1, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 0]]
grid_1 = [[0, 0, 0, 0], [1, 0, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]
print(numEnclaves(grid_1))
