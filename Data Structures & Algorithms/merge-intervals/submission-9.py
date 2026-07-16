class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        heap = intervals
        heapq.heapify(heap)
        res = []

        while len(heap) > 1:
            x = heapq.heappop(heap)
            if x[1] >= heap[0][0]:
                tmp = [
                    min(x[0], heap[0][0]),
                    max(x[1], heap[0][1])
                ]
                heapq.heappop(heap)
                heapq.heappush(heap, tmp)
            else:
                res.append(x)

        res.append(heap[0])
        return res
