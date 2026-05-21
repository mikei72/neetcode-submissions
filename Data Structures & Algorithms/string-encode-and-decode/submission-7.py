class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result += str(len(s))
            result += '#'
            result += s

        return result


    def decode(self, s: str) -> List[str]:
        if not s:
            return []

        length = 0
        result = []
        i = 0

        while i in range(len(s)):
            cur = ""
            while s[i] != '#':
                cur += s[i]
                i += 1
            length = int(cur)
            i += 1
            result.append(s[i:i + length])
            i += length
        
        return result
