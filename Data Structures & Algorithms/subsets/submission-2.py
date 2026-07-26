class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        for num in nums:
            tmp = []
            for r in res:
                tmp.append(r + [num])
            res += tmp

        return res 