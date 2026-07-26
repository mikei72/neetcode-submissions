class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        comb = []

        def dfs(start, total):
            if total == target:
                res.append(comb.copy())
                return
            elif start >= len(nums) or total > target:
                return

            comb.append(nums[start])
            dfs(start, total + nums[start])
            comb.pop()
            dfs(start + 1, total)

        dfs(0, 0)
        return res
        