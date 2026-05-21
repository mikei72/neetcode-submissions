class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            mid = (l + r) // 2

            if nums[mid] < nums[r]:
                r = mid
            else:
                l = mid + 1

        new_nums = nums[l:] + nums[:l]
        new_l, new_r = 0, len(nums) - 1

        while new_l <= new_r:
            mid = (new_l + new_r) // 2
            if new_nums[mid] > target:
                new_r = mid - 1
            elif new_nums[mid] < target:
                new_l = mid + 1
            else:
                return (mid + l) % len(nums)
            
        return -1