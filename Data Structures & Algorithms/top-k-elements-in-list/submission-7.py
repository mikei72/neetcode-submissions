class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        for num in nums:
            map[num] = 1 + map.get(num, 0)
        
        arr = []
        for num, count in map.items():
            arr.append([count, num])
        arr.sort()

        result = []
        for i in range(k):
            result.append(arr.pop()[1])
        
        return result