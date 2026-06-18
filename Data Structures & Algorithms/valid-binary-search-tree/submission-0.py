# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.is_bst = True

        def dfs(node):
            l_max, l_min = node.val, node.val
            r_max, r_min = node.val, node.val

            if node.left:
                l_max, l_min = dfs(node.left)
                if l_max >= node.val:
                    self.is_bst = False
            
            if node.right:
                r_max, r_min = dfs(node.right)
                if r_min <= node.val:
                    self.is_bst = False
            
            return r_max, l_min
            
        dfs(root)
            
        return self.is_bst