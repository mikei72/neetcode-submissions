class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        dp = [[-1] * len(nums) for _ in range(2)]

        def dfs(i, flag):
            if i >= len(nums) or (flag and i == len(nums) - 1):
                return 0
            
            if dp[flag][i] == -1:
                dp[flag][i] = max(dfs(i + 1, flag), dfs(i + 2, flag) + nums[i])
            
            return dp[flag][i]

        return max(dfs(0, True), dfs(1, False))