class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        heap = intervals
        heapq.heapify(heap)
        res = []

        while len(heap) > 1:
            x, y = heapq.heappop(heap), heapq.heappop(heap)
            if x[1] >= y[0]:
                tmp = [
                    min(x[0], y[0]),
                    max(x[1], y[1])
                ]
                heapq.heappush(heap, [min(x[0], y[0]), max(x[1], y[1])])
            else:
                res.append(x)
                heapq.heappush(heap, y)

        res.append(heap[0])
        return res
