import time
from typing import List


def countSquares(matrix: List[List[int]]) -> int:
    res = 0
    # Для единичных
    for line in matrix:
        res += line.count(1)
    # Для двоичных
    visited_2x2 = {()}
    visited_3x3 = {()}
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            visited_2x2.add((row, col))
            visited_3x3.add((row, col))
            stack = [(row, col)]
            while stack:
                row, col = stack.pop()
                if row + 1 < len(matrix) and col + 1 < len(matrix[0]):
                    x2 = [matrix[row][col], matrix[row + 1][col], matrix[row][col + 1], matrix[row + 1][col + 1]]
                    if x2.count(1) == 4 and x2 not in list(visited_2x2):
                        for index in x2:
                            visited_2x2.add(index)
                        stack.append((row, col))
                        res += 1
                        if row + 2 < len(matrix) and col + 2 < len(matrix[0]):
                            x3 = [matrix[row][col], matrix[row][col + 1], matrix[row][col + 2],
                                  matrix[row + 1][col], matrix[row + 1][col + 1], matrix[row + 1][col + 2],
                                  matrix[row + 2][col], matrix[row + 2][col + 1], matrix[row + 2][col + 2]]
                            if x3.count(1) == 9 and x3 not in list(visited_3x3):
                                for index in x3:
                                    visited_3x3.add(index)
                                stack.append((row, col))
                                res += 1
                        break
    return res


def countSquares_2(matrix: List[List[int]]) -> int:
    result = 0

    for i in range(len(matrix)):
        result += matrix[i].count(1)
    for i in range(len(matrix) - 1):
        for j in range(len(matrix[i]) - 1):
            if matrix[i][j] == 1 and matrix[i][j + 1] == 1:
                if matrix[i + 1][j] and matrix[i + 1][j + 1]:
                    result += 1
    for i in range(len(matrix) - 2):
        for j in range(len(matrix[i]) - 2):
            if matrix[i][j] == 1 and matrix[i][j + 1] == 1:
                if matrix[i][j + 2] == 1:
                    if matrix[i + 1][j] == 1 and matrix[i + 2][j] == 1:
                        if matrix[i + 1][j + 1] == 1 and matrix[i + 1][j + 2] == 1:
                            if matrix[i + 2][j + 1] == 1 and matrix[i + 2][j + 2] == 1:
                                result += 1
    return result


matrix = [[0, 1, 1, 1],
          [1, 1, 1, 1],
          [0, 1, 1, 1]]


def time_for_alg():
    t_start = time.time()
    print(countSquares(matrix))
    print("Моя программа: {0}".format((time.time() - t_start) * 100))
    t_start_2 = time.time()
    print(countSquares_2(matrix))
    print("Ярика программа: {0}".format((time.time() - t_start_2) * 100))


time_for_alg()
