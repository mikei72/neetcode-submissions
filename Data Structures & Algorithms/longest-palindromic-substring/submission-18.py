class Solution:
    def longestPalindrome(self, s: str) -> str:
        self.resIdx = 0
        self.resLen = 0

        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            
            if right - left - 1 > self.resLen:
                self.resLen = right - left - 1
                self.resIdx = left + 1 

        for i in range(len(s)):
            expand(i, i)
            
            if i + 1 < len(s) and s[i] == s[i + 1]:
                expand(i, i + 1)
        
        return s[self.resIdx : self.resIdx + self.resLen]
