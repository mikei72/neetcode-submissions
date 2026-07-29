class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        sub = []
        nums.sort()

        def dfs(depth):
            if depth == len(nums):
                res.append(sub.copy())
                return 
            
            sub.append(nums[depth])
            dfs(depth + 1)
            sub.pop()

            while depth + 1 < len(nums) and nums[depth] == nums[depth + 1]:
                depth += 1
            dfs(depth + 1)
        
        dfs(0)
        return res