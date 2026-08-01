class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dtc = {
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz"
        }

        res = []
        def dfs(count, phone):
            if count == len(digits):
                res.append(phone)
                return
            
            for c in dtc[digits[count]]:
                dfs(count + 1, phone + c)
            
        if digits:
            dfs(0, "")
        return res