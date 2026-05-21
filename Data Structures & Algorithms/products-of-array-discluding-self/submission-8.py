class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)
        product_all = 1
        zero_count = 0

        for num in nums:
            if num:
                product_all *= num
            else: 
                zero_count += 1

        if zero_count > 1:
            return result

        for i, num in enumerate(nums):
            if zero_count:
                if not num:
                    result[i] = product_all
                else:
                    continue
            else:
                result[i] = product_all // nums[i]

        return result