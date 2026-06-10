# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        
        while len(lists) > 1:
            merged = []
            for i in range(0, len(lists), 2):
                if (i + 1) < len(lists):
                    l1 = lists[i]
                    l2 = lists[i + 1]
                    merged.append(self.mergeLists(l1, l2))
                else:
                    merged.append(lists[i])
            lists = merged
        
        return lists[0]


    def mergeLists(self, l1, l2):
        node = ListNode(0)
        cur = node
    
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        
        cur.next = l1 if l1 else l2

        return node.next