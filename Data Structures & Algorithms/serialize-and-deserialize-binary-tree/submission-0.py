# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return 'n'

        q = deque([root])

        res = []
        
        while q:
            node = q.popleft()
            if node:
                res.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
            else:
                res.append('n')
        
        return ",".join(res)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data == "n":
            return None

        vals = data.split(',')
        root = TreeNode(vals[0])
        cur = 1
        q = deque([root])

        while q:
            node = q.popleft()

            if vals[cur] != 'n':
                node.left = TreeNode(int(vals[cur]))
                q.append(node.left)
            cur += 1

            if vals[cur] != 'n':
                node.right = TreeNode(int(vals[cur]))
                q.append(node.right)
            cur += 1

        return root

