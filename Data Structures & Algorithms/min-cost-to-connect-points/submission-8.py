class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        visit = [False] * n
        dist = [float("inf")] * n

        res, edges = 0, 0
        node = 0
        while edges < n - 1:
            visit[node] = True
            next = -1
            for i in range(n):
                if visit[i]:
                    continue
                d = abs(points[i][0] - points[node][0]) + abs(points[i][1] - points[node][1])
                dist[i] = min(dist[i], d)
                if next == -1 or dist[i] < dist[next]:
                    next = i
            
            res += dist[next]
            node = next
            edges += 1
        
        return res