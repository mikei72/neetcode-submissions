class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        dp1, dp2 = 1, 2
        for i in range(3, n + 1):
            tmp = dp1 + dp2
            dp1, dp2 = dp2, tmp
        return dp2