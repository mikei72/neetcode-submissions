# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def getKth(self, curr, k):
            while curr and k > 0:
                curr = curr.next
                k -= 1
            return curr

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
            
        dummy = ListNode(0, head)
        groupPrev = dummy

        while True:
            kth = self.getKth(groupPrev, k)
            if not kth:
                break

            groupNext = kth.next
            
            prev = groupNext
            cur = groupPrev.next

            groupPrev.next = kth
            groupPrev = cur

            for i in range(k):
                tmp = cur.next
                cur.next = prev
                prev = cur
                cur = tmp

        return dummy.next



            
        
        return head