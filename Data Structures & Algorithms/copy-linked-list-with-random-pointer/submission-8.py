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
        if not head:
            return None
            
        randMap = {None: None}
        cur = head
        while cur:
            randMap[cur] = Node(cur.val)
            cur = cur.next

        cur = head
        while cur:
            randMap[cur].next = randMap[cur.next]
            randMap[cur].random = randMap[cur.random]
            cur = cur.next
        
        return randMap[head]

            