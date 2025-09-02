class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = [0] * 32

        for n in nums:
            for i in range(32):
                count[i] += (n >> i) & 1

        res = 0
        for i, b in enumerate(count):
            if b % 3:
                res |= (1 << i)

        return res

