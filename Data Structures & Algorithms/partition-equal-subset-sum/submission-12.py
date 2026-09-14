class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        
        target = total // 2

        memo = [[False] * (target + 1) for _ in range(len(nums))]
        for i in range(len(nums)):
            memo[i][0] = True

        for i in range(len(nums)):
            for j in range(target + 1):
                if nums[i] <= j:
                    memo[i][j] = memo[i - 1][j] or memo[i - 1][j - nums[i]]
                else:
                    memo[i][j] = memo[i - 1][j]
        
        return memo[len(nums) - 1][target]