class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        existed = {}

        for i, num in enumerate(nums):
            diff = target - num

            if diff in existed:
                return [existed[diff], i]
            
            existed[num] = i