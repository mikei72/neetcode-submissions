class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        fresh_count = 0
        q = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh_count += 1
        if not fresh_count:
            return 0

        def rot(r, c):
            if min(r, c) < 0 or r >= ROWS or c >= COLS or grid[r][c] != 1:
                return 0
            q.append((r, c))
            grid[r][c] = 2
            return 1
         
        minutes = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                fresh_count -= rot(r + 1, c)
                fresh_count -= rot(r - 1, c)
                fresh_count -= rot(r, c + 1)
                fresh_count -= rot(r, c - 1) 
            minutes += 1
            if not fresh_count:
                break

        return minutes if not fresh_count else -1
        
        