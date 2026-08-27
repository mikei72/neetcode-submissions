class Solution:
    def numDecodings(self, s: str) -> int:
        dp1, dp2 = 1, 0

        for i in range(len(s) - 1, -1, -1):
            if s[i] == '0':
                tmp = 0
            else:
                tmp = dp1
            
            if i + 1 < len(s) and (s[i] == "1" or s[i] == "2" and s[i + 1] <= '6'):
                tmp += dp2
            
            dp1, dp2 = tmp, dp1
        
        return dp1

