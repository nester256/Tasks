def getKth(lo: int, hi: int, k: int) -> int:
    nums = []
    power = []
    for i in range(lo, hi + 1):
        nums.append(i)
    for n in nums:
        counter = 0
        while n != 1:
            counter += 1
            if n % 2 == 0:
                n /= 2
            else:
                n = 3 * n + 1
        power.append(counter)
    dic = dict(zip(nums, power))
    result = sorted(dic.items(), key=lambda x: (x[1], x[0]))
    return result[k - 1][0]


print(getKth(lo=7, hi=11, k=4))
print(getKth(lo=12, hi=15, k=2))
