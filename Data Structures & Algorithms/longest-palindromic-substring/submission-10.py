class Solution:
    def longestPalindrome(self, s: str) -> str:
        resIdx = 0
        resLen = 0

        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                length = r - l + 1
                if length > resLen:
                    resLen = length
                    resIdx = l
            
                l -= 1
                r += 1

            if i + 1 < len(s) and s[i] == s[i + 1]:
                l, r = i, i + 1
                while l >= 0 and r < len(s) and s[l] == s[r]:
                    length = r - l + 1
                    if length > resLen:
                        resLen = length
                        resIdx = l
                
                    l -= 1
                    r += 1
        
        return s[resIdx : resIdx + resLen]
