class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class PrefixTree:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c not in cur.children:
                new = TrieNode()
                cur.children[c] = new
            cur = cur.children[c]
        
        cur.is_end = True

    def search(self, word: str) -> bool:
        cur = self.root

        for c in word:
            if c not in cur.children:
                return False

            cur = cur.children[c]
        
        if cur.is_end:
            return True
        else:
            return False
        

    def startsWith(self, prefix: str) -> bool:
        cur = self.root

        for c in prefix:
            if c not in cur.children:
                return False
            
            cur = cur.children[c]
        
        return True
        