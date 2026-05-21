class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        area = 0

        for i in range(len(height)):
            while stack and height[i] >= height[stack[-1]]:
                bottom = height[stack.pop()]
                if stack:
                    right = height[i]
                    left = height[stack[-1]]
                    h = min(right, left) - bottom
                    w = i - stack[-1] - 1
                    area += h * w
            stack.append(i)
            
        return area