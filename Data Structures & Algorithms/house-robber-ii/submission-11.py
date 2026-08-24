class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def dfs(i, end, dp):
            if i >= end:
                return 0
            
            if dp[i] == -1:
                dp[i] = max(dfs(i + 1, end, dp), dfs(i + 2, end, dp) + nums[i])
            
            return dp[i]
        
        return max(dfs(0, len(nums) - 1, [-1] * len(nums)), dfs(1, len(nums), [-1] * len(nums)))