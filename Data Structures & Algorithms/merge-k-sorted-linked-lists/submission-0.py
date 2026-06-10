# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class NodeWrapper:
    def __init__(self, node):
        self.node = node
    
    def __lt__(self, other):
        return self.node.val < other.node.val

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        
        minHeap = []

        result = ListNode(0)
        cur = result

        for li in lists:
            if li:
                heapq.heappush(minHeap, NodeWrapper(li))
            
        while minHeap:
            nw = heapq.heappop(minHeap)
            cur.next = nw.node
            cur = cur.next
        
            if nw.node.next:
                heapq.heappush(minHeap, NodeWrapper(nw.node.next))
            
        return result.next