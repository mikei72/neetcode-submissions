class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList or beginWord == endWord:
            return 0
        m = len(wordList[0])
        wordSet = set(wordList)
        qb, qe = deque([beginWord]), deque([endWord])
        fromBegin, fromEnd = {beginWord: 1}, {endWord: 1}

        letters = set()
        for w in wordSet:
            for c in w:
                letters.add(c)

        while qb and qe:
            if len(qb) > len(qe):
                qb, qe = qe, qb
                fromBegin, fromEnd = fromEnd, fromBegin
            for _ in range(len(qb)):
                word = qb.popleft()
                steps = fromBegin[word]
                for i in range(m):
                    for c in letters:
                        if c == word[i]:
                            continue
                        nei = word[:i] + c + word[i + 1:]
                        if nei not in wordSet:
                            continue
                        if nei in fromEnd:
                            return steps + fromEnd[nei]
                        if nei not in fromBegin:
                            fromBegin[nei] = steps + 1
                            qb.append(nei)
        return 0