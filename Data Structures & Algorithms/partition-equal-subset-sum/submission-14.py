class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        
        target = total // 2

        dp1 = [False] * (target + 1)
        dp2 = [False] * (target + 1)
        dp1[0] = True

        for i in range(len(nums)):
            for j in range(1, target + 1):
                if nums[i] <= j:
                    dp2[j] = dp1[j] or dp1[j - nums[i]]
                else:
                    dp2[j] = dp1[j]
            dp1, dp2 = dp2, dp1
        
        return dp1[target]