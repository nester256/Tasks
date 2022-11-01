def minimumAbsDifference(arr: list[int]) -> list[list[int]]:
    arr = sorted(arr)
    min_el = 2 ** 31
    new_list = []
    for i in range(len(arr) - 1):
        if arr[i + 1] - arr[i] < min_el:
            min_el = arr[i + 1] - arr[i]
    for i in range(len(arr) - 1):
        if arr[i + 1] - arr[i] == min_el:
            new_list += [[arr[i], arr[i + 1]]]
    return new_list


print(minimumAbsDifference([3, 8, -10, 23, 19, -4, -14, 27]))
print(minimumAbsDifference([1, 3, 6, 10, 15]))
