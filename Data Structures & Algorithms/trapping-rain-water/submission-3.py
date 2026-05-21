class Solution:
    def trap(self, height: List[int]) -> int:
        length = len(height)
        if length < 3:
            return 0

        l_max = 0

        r_max = [0] * length
        for i in range(length - 2, 0, -1):
            if i == length - 2:
                r_max[i] = height[length - 1]
            else:
                r_max[i] = max(r_max[i + 1], height[i + 1])

        area = 0

        for i in range(1, length - 1):
            l_max = max(l_max, height[i - 1])
            wall = min(l_max, r_max[i]) 
            if wall > height[i]:
                area += wall - height[i]
            
        return area