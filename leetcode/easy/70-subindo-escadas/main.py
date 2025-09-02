def dp(mtx: list[list], current):
    if current < 0:
        return 0
    if current == 0:
        return 1
    
    if mtx[current] == -1:
        mtx[current] = dp(mtx, current - 1) + dp(mtx, current - 2)

    return mtx[current]

class Solution:
    def climbStairs(self, n: int) -> int:
        mtx = [-1] * (n + 1)
        return dp(mtx, n)
