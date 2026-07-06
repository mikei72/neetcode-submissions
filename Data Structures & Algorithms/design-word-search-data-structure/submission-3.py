class Node:
    def __init__(self):
        self.child = {}
        self.is_end = False

class WordDictionary:
    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c not in cur.child:
                cur.child[c] = Node()
            cur = cur.child[c]
        
        cur.is_end = True

    def search(self, word: str) -> bool:
        q = deque([(self.root, 0)])  # (node, index)

        while q:
            node, i = q.popleft()

            # 已经匹配到结尾
            if i == len(word):
                if node.is_end:
                    return True
                continue

            c = word[i]

            if c == ".":
                # 扩展所有子节点
                for child in node.child.values():
                    q.append((child, i + 1))
            else:
                if c in node.child:
                    q.append((node.child[c], i + 1))

        return False
