from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1] * len(nums)

        acc = 1
        for i in range(len(nums)):
            answer[i] *= acc
            acc *= nums[i]
        
        acc = 1
        for i in range(len(nums) - 1, -1, -1):
            answer[i] *= acc
            acc *= nums[i]
        
        return answer