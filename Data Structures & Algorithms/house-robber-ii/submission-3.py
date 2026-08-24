class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def dp(start, end):
            dp1, dp2 = 0, 0
            for num in nums[start : end]:
                tmp = max(dp2, dp1 + num)
                dp1 = dp2
                dp2 = tmp
            return dp2

        return max(dp(1, len(nums)), dp(0, len(nums) - 1))