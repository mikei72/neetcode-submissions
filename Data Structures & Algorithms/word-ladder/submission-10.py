class Solution:
    def differByOne(self, s1, s2):
        diff = 0
        for a, b in zip(s1, s2):
            if a != b:
                diff += 1
            if diff > 1:
                break
        return diff == 1

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList or beginWord == endWord:
            return 0
        
        wordList.append(beginWord)
        
        map = {s : [] for s in wordList}

        for i in range(len(wordList)):
            for j in range(i + 1, len(wordList)):
                a, b = wordList[i], wordList[j]
                if self.differByOne(a, b):
                    map[a].append(b)
                    map[b].append(a)

        visited = set()

        res = 0
        q = deque([beginWord])
        while q:
            res += 1
            for _ in range(len(q)):
                node = q.popleft()
                if node == endWord:
                    return res

                visited.add(node)

                for nei in map[node]:
                    if nei not in visited:
                        q.append(nei)

        return 0
