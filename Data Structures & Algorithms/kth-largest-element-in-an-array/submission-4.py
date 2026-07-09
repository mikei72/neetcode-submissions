class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def partition(l, r):
            i = l
            for j in range(l, r):
                if nums[j] <= nums[r]:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
            
            nums[i], nums[r] = nums[r], nums[i]
            return i

        target = len(nums) - k

        L, R = 0, len(nums) - 1
        pivot = len(nums)
        while pivot != target:
            pivot = partition(L, R)
            if pivot < target:
                L = pivot + 1
            else:
                R = pivot - 1

        return nums[target]