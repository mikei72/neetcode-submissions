class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        map = defaultdict(list)
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                map[i].append((dist, j))
                map[j].append((dist, i))
        
        res = 0
        visit = set()
        heap = [[0, 0]]
        while len(visit) < n:
            dist, i = heapq.heappop(heap)
            if i in visit:
                continue
            res += dist
            visit.add(i)
            for neicost, nei in map[i]:
                heapq.heappush(heap, [neicost, nei])
        
        return res