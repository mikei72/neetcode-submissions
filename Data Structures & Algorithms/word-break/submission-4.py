class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = {len(s) : True}

        def dfs(i):
            if i in dp:
                return dp[i]
            
            for w in wordDict:
                if ((i + len(w)) <= len(s) and s[i : i + len(w)] == w):
                    if dfs(i + len(w)):
                        dp[i] = True
                        return True
            
            dp[i] = False
            return False
        
        return dfs(0)