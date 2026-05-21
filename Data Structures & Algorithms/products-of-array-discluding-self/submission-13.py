class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        prefix = [0] * (length - 1)
        suffix = [0] * (length - 1)

        prefix[0] = nums[0]
        suffix[0] = nums[length - 1]
        for i in range(1, length - 1):
            prefix[i] = prefix[i - 1] * nums[i]
            suffix[i] = suffix[i - 1] * nums[length - i - 1]
        
        result = [0] * length
        result[0] = suffix[length - 2]
        for i in range(1, length):
            result[i] = prefix[i - 1] * suffix[length - i - 2]
        result[length - 1] = prefix[length - 2]

        return result