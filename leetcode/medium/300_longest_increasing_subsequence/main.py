from math import inf
from bisect import bisect_left

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lis = [inf] * (len(nums) + 1)
        r = 0
        for n in nums:
            pos = bisect_left(lis, n)
            lis[pos] = n
            r = max(r, pos)
        return r + 1

                
