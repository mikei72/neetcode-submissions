class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cs = {}
        maxcount = 0
        left = 0

        for r in range(len(s)):
            if s[r] in cs:
                left = max(cs[s[r]] + 1, left)
            cs[s[r]] = r
            maxcount = max(maxcount, r - left + 1)
        
        return maxcount
            