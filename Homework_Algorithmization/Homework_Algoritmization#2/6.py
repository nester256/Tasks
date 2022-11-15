
def rob(nums):
    def simple_rob(nums):
        rob = 0
        n_rob = 0
        for num in nums:
            rob, n_rob = n_rob + num, max(rob, n_rob)
        return max(rob, n_rob)
    if not nums:
        return 0
    elif len(nums) == 1:
        return nums[0]
    else:
        return max(simple_rob(nums[1:]), simple_rob(nums[:-1]))


print(rob([1, 2, 3, 1]))
