class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        suf, pre = 0, 0
        res = nums[0]
        n = len(nums)

        for i in range(len(nums)):
            suf = nums[i] * (suf or 1)
            pre = nums[n - 1 - i] * (pre or 1)
            res = max(res, suf, pre)

        return res