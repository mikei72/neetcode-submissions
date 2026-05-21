class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        max_amount = 0

        while l < r:
            if heights[l] <= heights[r]:
                max_amount = max(max_amount, heights[l] * (r - l))
                l += 1
            else:
                max_amount = max(max_amount, heights[r] * (r - l))
                r -= 1
        
        return max_amount