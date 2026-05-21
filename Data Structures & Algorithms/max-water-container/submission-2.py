class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        max_amount = 0

        while l < r:
            hl, hr = heights[l], heights[r]
            if hl <= hr:
                max_amount = max(max_amount, hl * (r - l))
                l += 1
            else:
                max_amount = max(max_amount, hr * (r - l))
                r -= 1
        
        return max_amount