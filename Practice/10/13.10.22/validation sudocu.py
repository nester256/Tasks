ex = [[2, 9, 3, 4, 5, 7, 6, 8, 1],
      [4, 7, 5, 1, 8, 6, 3, 9, 2],
      [1, 6, 8, 3, 9, 2, 7, 4, 5],
      [9, 4, 2, 5, 7, 1, 8, 6, 3],
      [3, 8, 1, 6, 2, 9, 5, 7, 4],
      [6, 5, 7, 8, 3, 4, 1, 2, 9],
      [7, 2, 6, 9, 1, 3, 4, 5, 8],
      [5, 1, 4, 2, 6, 8, 9, 3, 7],
      [8, 3, 9, 7, 4, 5, 2, 1, 6]]

ex_1 = ([[5, 3, 4, 6, 7, 8, 9, 1, 2],
         [6, 7, 2, 1, 9, 5, 3, 4, 8],
         [1, 9, 8, 3, 4, 2, 5, 6, 7],
         [8, 5, 9, 7, 6, 1, 4, 2, 3],
         [4, 2, 6, 8, 5, 3, 7, 9, 1],
         [7, 1, 3, 9, 2, 4, 8, 5, 6],
         [9, 6, 1, 5, 3, 7, 2, 8, 4],
         [2, 8, 7, 4, 1, 9, 6, 3, 5],
         [3, 4, 5, 2, 8, 6, 1, 7, 9]])


def check_validation_cudoku(board):
    transported = list(zip(*board))
    # Первая проверка по столбцам
    for row in board:
        if 0 in row:
            return False

    for row in board:
        if len(set(row)) != 9:
            return False

    for col in transported:
        if len(set(col)) != 9:
            return False

    for i in range(3):
        for k in range(3):
            square = [board[m][n] for m in range(i * 3, (i + 1) * 3)
                      for n in range(k * 3, (k + 1) * 3)]
            if len(set(square)) != 9:
                return False
    return True


print(check_validation_cudoku(ex))
