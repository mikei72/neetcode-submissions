# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
            
        self.num = 0

        def dfs(node, prev_max):
            if node.val >= prev_max:
                self.num += 1
                prev_max = node.val

            if node.left:
                dfs(node.left, prev_max)
            if node.right:
                dfs(node.right, prev_max)

        dfs(root, float('-inf'))

        return self.num 