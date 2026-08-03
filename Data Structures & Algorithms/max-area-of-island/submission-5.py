class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        max_area = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(r, c):
            area = 1
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or not grid[r][c]:
                return 0
            
            grid[r][c] = 0
            for dr, dc in directions:
                area += dfs(r + dr, c + dc)

            print(area)
            return area

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    max_area = max(max_area, dfs(i, j))
        
        return max_area
