class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        n = len(words)
        map = {c : set() for w in words for c in w}

        for i in range(n - 1):
            w1, w2 = words[i], words[i + 1]
            minLen = min(len(w1), len(w2))

            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""

            for j in range(minLen):
                if w1[j] != w2[j]:
                    map[w1[j]].add(w2[j])
                    break

        visited = {}
        res = []
        
        def dfs(char):
            if char in visited:
                return visited[char]

            visited[char] = True
            for nei in map[char]:
                if dfs(nei):
                    return True
            
            visited[char] = False
            res.append(char)

        for c in map:
            if dfs(c): 
                return ""
            
        res.reverse()
        return "".join(res)
        