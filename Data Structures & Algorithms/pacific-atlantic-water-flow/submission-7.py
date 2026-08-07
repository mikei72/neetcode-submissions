class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pac, atl = set(), set()
        ROWS, COLS = len(heights), len(heights[0])

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def dfs(r, c, visit):
            visit.add((r, c))

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (min(nr, nc) >= 0 and nr < ROWS and nc < COLS 
                    and heights[nr][nc] >= heights[r][c] and (nr, nc) not in visit):
                    dfs(nr, nc, visit)
            
        for c in range(COLS):
            dfs(0, c, pac)
            dfs(ROWS - 1, c, atl)
        for r in range(ROWS):
            dfs(r, 0, pac)
            dfs(r, COLS - 1, atl)
        
        res = []
        """for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])"""
        for cell in pac:
            if cell in atl:
                res.append([cell[0], cell[1]])
        return res