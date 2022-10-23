list_for_psh = [[1, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                [1, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                [1, 0, 0, 1, 1, 1, 0, 0, 0, 0],
                [1, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
                [0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 1, 0, 0, 1, 0, 1, 0, 0],
                [1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]


def check_valid_dsh(list_vs):
    count_all, count_1, count_2, count_3, count_4 = 0, 0, 0, 0, 0
    # По горизонтали
    for i in range(10):
        for j in range(10):
            if list_vs[i][j] == 1:
                count_all += 1
                if 1 <= i < 10 and 1 <= j < 10:
                    list_vs[i + 1]

    print(count_all)
    return


check_valid_dsh(list_for_psh)
