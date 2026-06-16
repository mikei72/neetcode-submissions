# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque([root])
        res = []

        while q:
            q_len = len(q)
            l_trav = []
            for i in range(q_len):
                node = q.popleft()
                if node:
                    q.append(node.left)
                    q.append(node.right)
                    l_trav.append(node.val)
            if l_trav:
                res.append(l_trav)


        return res
            