class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        for num in nums:
            map[num] = 1 + map.get(num, 0)
        
        heap = []
        for num in map.keys():
            heapq.heappush(heap, [map[num], num])
            if(len(heap) > k):
                heapq.heappop(heap)
            
        result = []
        for i in range(k):
            result.append(heapq.heappop(heap)[1])
        return result