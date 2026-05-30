class Solution:
    def minWindow(self, s: str, t: str) -> str:
        countT = {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        have, need = 0, len(countT)
        window = {}
        l = 0
        resStart, resLen = -1, float('infinity')
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in countT and window[c] == countT[c]:
                have += 1

            while have == need:
                if r - l + 1 < resLen:
                    res = l
                    resLen = r - l + 1

                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1

        if resLen != float('infinity'):
            l, r = res, res + resLen - 1 
            return s[l : r + 1]
        else:
            return ""
            

