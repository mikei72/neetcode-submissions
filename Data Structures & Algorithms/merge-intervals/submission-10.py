class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        heap = intervals
        heapq.heapify(heap)
        res = []

        while heap:
            current = heapq.heappop(heap)

            while heap and current[1] >= heap[0][0]:
                current[1] = max(current[1], heapq.heappop(heap)[1])

            res.append(current)

        return res
