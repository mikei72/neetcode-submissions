class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
            
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
        
        res = [""]
        
        for digit in digits:
            tmp = []
            for phone in res:
                for c in dtc[digit]:
                    tmp.append(phone + c)
            res = tmp
        
        return res
