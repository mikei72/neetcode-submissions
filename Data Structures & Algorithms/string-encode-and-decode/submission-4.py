class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""

        lengths = []
        for s in strs:
            lengths.append(len(s))
        
        result = ""
        for length in lengths:
            result += str(length)
            result += ','
        result += '#'
        result += ''.join(strs)

        return result


    def decode(self, s: str) -> List[str]:
        if not s:
            return []

        lengths = []
        result = []
        i = 0

        while s[i] != '#':
            cur = ""
            while s[i] != ',':
                cur += s[i]
                i += 1
            lengths.append(int(cur))
            i += 1
        i += 1

        for length in lengths:
            result.append(s[i:i + length])
            i += length
        
        return result
