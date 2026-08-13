class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        map = [[] for _ in range(n)]
        for u, v in edges:
            map[u].append(v)
            map[v].append(u)
        
        visited = [False] * n
        def dfs(node):
            for nei in map[node]:
                if not visited[nei]:
                    visited[nei] = True
                    dfs(nei)
        
        count = 0
        for i in range(n):
            if not visited[i]:
                dfs(i)
                count += 1
        return count
