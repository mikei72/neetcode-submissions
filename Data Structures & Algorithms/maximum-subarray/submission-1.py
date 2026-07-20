class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum, curSum = nums[0], 0

        for num in nums:
            if curSum < 0:
                curSum = 0
            curSum += num
            sum = max(sum, curSum)
        
        return sum