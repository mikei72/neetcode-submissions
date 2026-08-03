class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        max_area = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def bfs(r, c):
            area = 1
            q = deque()
            q.append((r, c))
            grid[r][c] = 0

            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or not grid[nr][nc]:
                        continue
                    q.append((nr, nc))
                    grid[nr][nc] = 0
                    area += 1
            
            return area

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    max_area = max(max_area, bfs(i, j))
        
        return max_area
