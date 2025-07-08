from typing import List

class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        n = len(nums)
        freq = {}         # frequency dictionary for current window
        pairs = 0         # current number of pairs in the window
        res = 0           # result: count of good subarrays
        l = 0             # left pointer
        
        # r is the right pointer, we iterate through all indices
        for r in range(n):
            # Add nums[r] to the window
            count = freq.get(nums[r], 0)
            pairs += count       # each occurrence already in window forms a new pair with nums[r]
            freq[nums[r]] = count + 1
            
            # While current window [l, r] has at least k pairs, we can shift l
            while pairs >= k and l <= r:
                # All subarrays starting at l and ending at any index from r to n - 1 are good.
                # (Because extending the subarray cannot reduce the number of pairs.)
                res += (n - r)
                
                # Remove element nums[l] from the window and update pairs
                f = freq[nums[l]]
                freq[nums[l]] = f - 1
                # Removing this element loses the pairs it formed with the remaining copies.
                pairs -= (f - 1)
                l += 1

        return res

# Testing the solution with the provided examples
if __name__ == '__main__':
    sol = Solution()
    
    # Example 1:
    nums1 = [1, 1, 1, 1, 1]
    k1 = 10
    print("Output for Example 1:", sol.countGood(nums1, k1))  # Expected output: 1

    # Example 2:
    nums2 = [3, 1, 4, 3, 2, 2, 4]
    k2 = 2
    print("Output for Example 2:", sol.countGood(nums2, k2))  # Expected output: 4
