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

        def dfs(node, prev_max):
            if node.val >= prev_max:
                res = 1
                prev_max = node.val
            else:
                res = 0

            if node.left:
                res += dfs(node.left, prev_max)
            if node.right:
                res += dfs(node.right, prev_max)

            return res

        return dfs(root, root.val) 