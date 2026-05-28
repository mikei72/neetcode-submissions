class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = prices[0]
        maxP = 0

        for p in prices:
            lowest = min(lowest, p)
            maxP = max(maxP, p - lowest)
        
        return maxP