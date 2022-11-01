def findKthLargest(nums: list[int], k: int) -> int:
    nums = sorted(nums, reverse=True)
    return nums[k - 1]


print(findKthLargest(nums=[3, 2, 3, 1, 2, 4, 5, 5, 6], k=4))
print(findKthLargest(nums=[3, 2, 1, 5, 6, 4], k=2))
