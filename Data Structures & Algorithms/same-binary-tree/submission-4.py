# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, root, l):
        if not root:
            l.append(None)
        else:
            l.append(root.val)
            self.dfs(root.left, l)
            self.dfs(root.right, l)

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        l1, l2 = [], []

        self.dfs(p, l1)
        self.dfs(q, l2)

        return l1 == l2