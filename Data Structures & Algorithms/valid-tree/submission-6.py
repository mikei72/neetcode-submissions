class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        map = [[] for i in range(n)]
        for d1, d2 in edges:
            map[d1].append(d2)
            map[d2].append(d1)

        visited = set()
        def dfs(node, par):
            if node in visited:
                return False
            
            visited.add(node)

            for next in map[node]:
                if next == par:
                    continue
                if not dfs(next, node):
                    return False

            return True
        

        return dfs(0, -1) and len(visited) == n

