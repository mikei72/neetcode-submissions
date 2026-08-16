class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList or beginWord == endWord:
            return 0

        words, res = set(wordList), 0
        q = deque([beginWord])

        letters = {c for w in words for c in w}

        while q:
            res += 1
            for _ in range(len(q)):
                node = q.popleft()
                if node == endWord:
                    return res
                
                for i in range(len(node)):
                    for c in letters:
                        if c == node[i]:
                            continue
                        nei = node[:i] + c + node[i + 1:]
                        if nei in words:
                            q.append(nei)
                            words.remove(nei)
        return 0