class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        minv, maxv = 1, piles[-1]
        rate = -1

        while minv <= maxv:
            v = (minv + maxv) // 2
            time = 0
            for p in piles:
                time += (p + v - 1) // v
            if time <= h:
                rate = min(rate, v) if rate > 0 else v
                maxv = v - 1
            else:
                minv = v + 1
        
        return rate
