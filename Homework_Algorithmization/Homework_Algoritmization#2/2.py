def getMaximumGenerated(n: int) -> int:
    nums = [0, 1]
    i = 1
    if n >= 2:
        nums = nums + [0] * (n - 1)
        while (i * 2) + 1 < n + 2:
            if i % 2 != 0:
                nums[i * 2] = nums[i]
                if i * 2 < n:
                    nums[i * 2 + 1] = nums[i] + nums[i + 1]
                i += 1
            else:
                nums[i * 2 + 1] = nums[i] + nums[i + 1]
                nums[i * 2] = nums[i]
                i += 1
    return max(nums)


print(getMaximumGenerated(0))
