# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, root):
        if not root:
            return (0, True)

        l, lb = self.dfs(root.left)
        r, rb = self.dfs(root.right)

        is_balance = abs(l - r) <= 1

        return (1 + max(l, r), lb and rb and is_balance)


    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root)[1]