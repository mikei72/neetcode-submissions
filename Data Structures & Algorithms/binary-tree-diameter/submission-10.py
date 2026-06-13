# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        map = {None: (0, 0)}
        stack = [root]

        while stack:
            node = stack[-1]

            if node.left and node.left not in map:
                stack.append(node.left)
            elif node.right and node.right not in map:
                stack.append(node.right)
            else:
                node = stack.pop()
                lh, ld = map[node.left]
                rh, rd = map[node.right]
                map[node] = (1 + max(lh, rh), max(lh + rh, ld, rd))
        
        return map[root][1]