class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        map = [[-1] * (n + 1) for _ in range(n)]

        def dfs(i, prev):
            if i >= n:
                return 0
            
            if map[i][prev + 1] == -1:
                map[i][prev + 1] = dfs(i + 1, prev)

                if prev == -1 or nums[i] > nums[prev]:
                    map[i][prev + 1] = max(map[i][prev + 1], 1 + dfs(i + 1, i))

            return map[i][prev + 1]
            
        return dfs(0, -1)