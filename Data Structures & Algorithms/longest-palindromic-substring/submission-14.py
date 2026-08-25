class Solution:
    def longestPalindrome(self, s: str) -> str:
        bestl = 0
        bestr = 0

        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return left + 1, right - 1

        for i in range(len(s)):
            l, r = expand(i, i)
            if r - l > bestr - bestl:
                bestl, bestr = l, r
            
            if i + 1 < len(s) and s[i] == s[i + 1]:
                l, r = expand(i, i + 1)
                if r - l > bestr - bestl:
                    bestl, bestr = l, r
        
        return s[bestl : bestr + 1]
