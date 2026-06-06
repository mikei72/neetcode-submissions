"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        randMap = collections.defaultdict(lambda: Node(0))
        randMap[None] = None

        cur = head
        while cur:
            randMap[cur].val = cur.val
            randMap[cur].next = randMap[cur.next]
            randMap[cur].random = randMap[cur.random]
            cur = cur.next
        
        return randMap[head]

            