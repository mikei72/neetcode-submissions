class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        q = deque()
        degrees = [0] * n
        neibors = [[] for _ in range(n)]

        for u, v in edges:
            degrees[u - 1] += 1
            degrees[v - 1] += 1
            neibors[u - 1].append(v - 1)
            neibors[v - 1].append(u - 1)

        for i in range(n):
            if degrees[i] == 1:
                q.append(i)
        
        while q:
            node = q.popleft()
            degrees[node] -= 1

            for nei in neibors[node]:
                degrees[nei] -= 1
                if degrees[nei] == 1:
                    q.append(nei)
        
        for u, v in reversed(edges):
            if degrees[u - 1] == 2 and degrees[v - 1]:
                return [u, v]
        
        return []