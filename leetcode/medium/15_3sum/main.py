from bisect import bisect_left
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)

        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for k in range(n - 1, i + 1, -1):
                if k < n - 1 and nums[k] == nums[k + 1]:
                    continue

                target = -(nums[i] + nums[k])

                if target < nums[i + 1] or target > nums[k - 1]:
                    continue

                pos = bisect_left(nums, target, i + 1, k)
                if pos < k and nums[pos] == target:
                    res.append([nums[i], target, nums[k]])

        return res
