class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        se = {}
        for i, c in enumerate(s):
            if c not in se:
                se[c] = [i, i]
            else:
                se[c][1] = i
        
        res = []
        heap = []
        for k in se.keys():
            heapq.heappush(heap, se[k])
        
        while heap:
            current = heapq.heappop(heap)

            while heap and current[1] >= heap[0][0]:
                current[1] = max(current[1], heapq.heappop(heap)[1])
            
            res.append(current)

        print(res)
        
        return [x[1] - x[0] + 1 for x in res]