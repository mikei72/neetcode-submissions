class Solution:
    def jump(self, nums: List[int]) -> int:
        pos = 0
        count = 0
        
        while pos < len(nums) - 1:
            if pos + nums[pos] >= len(nums) - 1:
                return count + 1

            best_idx = pos
            for i in range(nums[pos]):
                cur = pos + i + 1
                if nums[cur] + cur >= nums[best_idx] + best_idx:
                    best_idx = cur
            
            pos = best_idx
            count += 1
            print(pos)

        return count
