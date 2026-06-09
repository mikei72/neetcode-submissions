class Node:
    def __init__(self, key=0, val=0):
        self.val, self.key = val, key
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.left, self.right = Node(), Node()
        self.left.next = self.right
        self.right.prev = self.left

        self.cap = capacity
        self.cache = {}

    def insert(self, key: int, value: int, node: Optional[Node] = None):
        if not node:
            node = Node(key, value)
            self.cache[key] = node

        prev = self.right.prev

        prev.next = node
        node.prev = prev

        self.right.prev = node
        node.next = self.right

    def delete(self, node: Optional[Node]) -> [int, int]:
        node.prev.next = node.next
        node.next.prev = node.prev

        return node.key, node.val

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        if self.cache[key].next != self.right:
            self.delete(self.cache[key])
            self.insert(-1, -1, self.cache[key])

        return self.cache[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.get(key)
            self.cache[key].val = value
        elif self.cap > 0:
            self.cap -= 1
            self.insert(key, value)
        else:
            k, v = self.delete(self.left.next)
            self.cache.pop(k)
            self.insert(key, value)


