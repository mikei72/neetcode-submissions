class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False

        memo = [[-1] * (sum(nums) // 2 + 1) for _ in range(len(nums))]

        def dfs(i, target):
            if i >= len(nums):
                return target == 0
            if target < 0:
                return False

            if memo[i][target] == -1:
                memo[i][target] = dfs(i + 1, target) or dfs(i + 1, target - nums[i])
            
            return memo[i][target]
        
        return dfs(0, sum(nums) // 2)