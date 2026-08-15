class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        map = [[] for _ in range(len(edges))]
        
        def dfs(node, par):
            if visited[node]:
                return True
            
            visited[node] = True
            for child in map[node]:
                if child != par:
                    if dfs(child, node):
                        return True
            
            return False

        for u, v in edges:
            map[u - 1].append(v - 1)
            map[v - 1].append(u - 1)
            visited = [False] * len(edges)
            if dfs(u - 1, -1):
                return [u, v]

        return None
        