# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        cur = head
        while cur:
            cur = cur.next
            length += 1
        
        num = length - n
        if num == 0:
            return head.next

        cur = ListNode(0, head)
        for i in range(num):
            cur = cur.next
        
        cur.next = cur.next.next

        return head