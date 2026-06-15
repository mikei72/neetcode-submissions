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

        lenSub = len(serial2)
        for i in range(len(serial1) - lenSub + 1):
            if serial1[i : i + lenSub] == serial2:
                return True

        return False