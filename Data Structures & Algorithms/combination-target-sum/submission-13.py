class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        comb = []
        nums.sort()

        def dfs(start, total):
            if total == target:
                res.append(comb.copy())
                return

            for i in range(start, len(nums)):
                num = nums[i]
                if total + num > target:
                    return

                comb.append(num)
                dfs(i, total + num)
                comb.pop()

        dfs(0, 0)
        return res
        