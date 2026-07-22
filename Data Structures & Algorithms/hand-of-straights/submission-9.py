class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False

        count = Counter(hand)
        
        heap = list(count.keys())
        heapq.heapify(heap)

        while heap:
            start = heap[0]

            for num in range(start, start + groupSize):
                if count[num] == 0:
                    return False
                
                count[num] -= 1

                if count[num] == 0:
                    if heap[0] != num:
                        return False
                    heapq.heappop(heap)
                
        return True