class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        map = {}
        res = 0

        maxf = 0
        l = 0
        for r in range(len(s)):
            map[s[r]] = 1 + map.get(s[r], 0)
            maxf = max(maxf, map[s[r]])

            while r - l + 1 - maxf > k:
                map[s[l]] -= 1
                l += 1 
            
            res = max(res, r - l + 1)

        return res
