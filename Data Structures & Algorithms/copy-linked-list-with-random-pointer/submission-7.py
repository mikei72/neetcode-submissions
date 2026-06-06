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

        cur = head
        while cur:
            cur.random = Node(cur.val, cur.random)
            cur = cur.next
        
        head2 = head.random

        cur = head
        while cur:
            cur2 = cur.random
            cur2.random = cur2.next.random if cur2.next else None
            cur = cur.next
        
        cur = head
        while cur:
            cur2 = cur.random
            cur.random = cur2.next
            cur2.next = cur.next.random if cur.next else None
            cur = cur.next
        
        return head2

            