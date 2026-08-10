class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        map = {i : [] for i in range(n)}
        for d1, d2 in sorted(edges):
            if not map[d2]:
                map[d1].append(d2)
            else:
                map[d2].append(d1)

        visited = set()
        
        def dfs(node):
            if node in visited:
                return False
            
            visited.add(node)

            flag = True
            for next in map[node]:
                flag = flag and dfs(next)

            return flag
        

        return dfs(0) and (len(visited) == n)

