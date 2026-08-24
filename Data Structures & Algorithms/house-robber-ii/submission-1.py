class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
            
        dp1, dp2 = 0, 0
        for num in nums[1:]:
            tmp = max(dp2, dp1 + num)
            dp1 = dp2
            dp2 = tmp
        max1 = dp2

        dp1, dp2 = 0, 0
        for num in nums[:len(nums) - 1]:
            tmp = max(dp2, dp1 + num)
            dp1 = dp2
            dp2 = tmp
        max2 = dp2

        return max(max1, max2)