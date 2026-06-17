# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = [(root, 1)]

        while stack:
            node, depth = stack.pop()

            if not node:
                continue

            if depth == len(res) + 1:
                res.append(node.val)
            
            stack.append((node.left, depth + 1))
            stack.append((node.right, depth + 1))
        
        return res