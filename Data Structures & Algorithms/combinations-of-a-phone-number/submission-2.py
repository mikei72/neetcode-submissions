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
        phone = []
        def dfs(count):
            if count == len(digits):
                if phone:
                    res.append("".join(phone))
                return
            
            for i in range(len(dtc[digits[count]])):
                phone.append(dtc[digits[count]][i])
                dfs(count + 1)
                phone.pop()
            
        dfs(0)
        return res