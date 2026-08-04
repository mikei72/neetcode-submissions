"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        map = {}
        q = deque([node])
        map[node] = Node(node.val)

        while q:
            n = q.popleft()
            for neigh in n.neighbors:
                if neigh not in map:
                    q.append(neigh)
                    map[neigh] = Node(neigh.val)
                map[n].neighbors.append(map[neigh]) 
        
        return map[node]