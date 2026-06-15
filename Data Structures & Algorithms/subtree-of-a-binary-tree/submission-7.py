# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def serialize(self, root):
        if not root:
            return "$#"

        left = self.serialize(root.left)
        right = self.serialize(root.right)
        
        return "$" + str(root.val) + left + right

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        serial1, serial2 = self.serialize(root), self.serialize(subRoot)

        if serial2 in serial1:
            return True
        else:
            return False