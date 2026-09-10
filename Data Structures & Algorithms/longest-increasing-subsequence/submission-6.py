class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        map = [-1] * n

        def dfs(i):
            if map[i] != -1:
                return map[i]
            
            res = 1
            for j in range(i + 1, n):
                if nums[i] < nums[j]:
                    res = max(res, 1 + dfs(j))
            
            map[i] = res
            return res
        
        return max(dfs(i) for i in range(n))