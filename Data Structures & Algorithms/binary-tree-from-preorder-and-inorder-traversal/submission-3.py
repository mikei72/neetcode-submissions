# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        indices = {v : i for i, v in enumerate(inorder)}

        self.prev_idx = 0
        def dfs(l, r):
            if l > r:
                return None

            node_val = preorder[self.prev_idx]
            self.prev_idx += 1
            
            idx = indices[node_val]

            root = TreeNode(node_val)

            root.left = dfs(l, idx - 1)
            root.right = dfs(idx + 1, r)

            return root

        return dfs(0, len(inorder) - 1)
