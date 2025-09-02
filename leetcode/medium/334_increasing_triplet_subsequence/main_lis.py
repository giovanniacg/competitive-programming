from math import inf
from bisect import bisect_left

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        lis = [inf] * 4
        
        for n in nums:
            pos = bisect_left(lis, n)
            if pos == 2:
                return True
            lis[pos] = n
        return False

