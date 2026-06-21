# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def getMax(self, node):
        if not node:
            return 0
        
        left = self.getMax(node.left)
        right = self.getMax(node.right)

        return max(0, node.val + max(left, right))

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = -float('inf')

        def dfs(node):
            if not node:
                return

            left = self.getMax(node.left)
            right = self.getMax(node.right)
            self.res = max(self.res, left + right + node.val)

            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return self.res