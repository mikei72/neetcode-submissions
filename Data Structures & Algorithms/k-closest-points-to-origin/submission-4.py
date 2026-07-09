class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = [math.sqrt(p[0]**2 + p[1]**2) for p in points]

        heap = []
        for i in range(len(distances)):
            heapq.heappush(heap, (-distances[i], i))
            if len(heap) > k:
                heapq.heappop(heap)
        
        res = []
        for h in heap:
            res.append(points[h[1]])
        
        return res