class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        minv, maxv = 1, max(piles)
        rate = maxv

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
