class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n - 1

        while l < r:
            if nums[l] < nums[r]:
                return nums[l]

            if l + 1 == r:
                return nums[r]

            mid = (l + r) // 2

            if nums[mid] < nums[r]:
                r = mid
            else:
                l = mid + 1
        
        return nums[l]
