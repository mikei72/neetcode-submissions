class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        for num in nums:
            if num in map.keys():
                map[num] += 1
            else:
                map[num] = 1
        
        arr = []
        for num, count in map.items():
            arr.append([count, num])
        arr.sort()

        result = []
        for i in range(k):
            result.append(arr.pop()[1])
        
        return result