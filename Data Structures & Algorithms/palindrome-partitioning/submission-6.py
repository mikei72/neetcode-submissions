class Solution:
    def isPalin(self, s) -> bool:
        for i in range(len(s) // 2):
            if s[i] != s[-i - 1]:
                return False
        
        return True


    def partition(self, s: str) -> List[List[str]]:
        res = []
        palin = []

        def dfs(i):
            if i >= len(s):
                res.append(palin.copy())
                return
        
            for j in range(i, len(s)):
                sub = s[i : j + 1]

                if self.isPalin(sub):
                    palin.append(sub)
                    dfs(j + 1)
                    palin.pop()

        dfs(0)
        return res

