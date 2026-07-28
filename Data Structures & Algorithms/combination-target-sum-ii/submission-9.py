class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        comb = []

        def dfs(i, total):
            if total == target:
                res.append(comb.copy())
                return 

            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j - 1]:
                    continue
                if total + candidates[j] > target:
                    break
                
                comb.append(candidates[j])
                dfs(j + 1, total + candidates[j])
                comb.pop()
        
        dfs(0, 0)
        return res
