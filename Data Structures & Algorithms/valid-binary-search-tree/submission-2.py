# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        q = deque()
        q.append((root, -1001, 1001))

        while q:
            node, min, max = q.popleft()
            if not node:
                continue
            
            if not (min < node.val < max):
                return False
            
            q.append((node.left, min, node.val))
            q.append((node.right, node.val, max))

        return True