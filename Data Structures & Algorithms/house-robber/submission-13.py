class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        dp1 = nums[0]
        dp2 = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            tmp = max(dp2, dp1 + nums[i])
            dp1 = dp2
            dp2 = tmp

        return dp2