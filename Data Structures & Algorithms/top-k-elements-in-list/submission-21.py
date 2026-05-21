class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        
        arr = []
        for num, cnt in count.items():
            arr.append([cnt, num])
        arr.sort(reverse=True)

        result = []
        for i in range(k):
            result.append(arr[i][1])
        return result
