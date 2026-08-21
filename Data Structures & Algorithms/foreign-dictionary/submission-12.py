class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        n = len(words)
        map = {c : set() for w in words for c in w}
        indegree = {c : 0 for c in map}

        for i in range(n - 1):
            w1, w2 = words[i], words[i + 1]
            minLen = min(len(w1), len(w2))

            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""

            for j in range(minLen):
                if w1[j] != w2[j]:
                    if w2[j] not in map[w1[j]]:
                        map[w1[j]].add(w2[j])
                        indegree[w2[j]] += 1
                    break

        q = deque([c for c in indegree if not indegree[c]])
        res = []

        while q:
            char = q.popleft()
            res.append(char)
            for nei in map[char]:
                indegree[nei] -= 1
                if not indegree[nei]:
                    q.append(nei)
        
        if len(res) != len(indegree):
            return ""
        
        return "".join(res)