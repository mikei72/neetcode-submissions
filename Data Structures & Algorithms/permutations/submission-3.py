class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        perm = []
        picked = [False] * len(nums)

        def dfs(length):
            if length == len(nums):
                res.append(perm.copy())
                return
            
            for i, num in enumerate(nums):
                if not picked[i]:
                    perm.append(num)
                    picked[i] = True
                    dfs(length + 1)
                    perm.pop()
                    picked[i] = False
        
        dfs(0)

        return res
            
