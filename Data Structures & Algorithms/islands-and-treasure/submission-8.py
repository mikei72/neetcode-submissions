class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        INF = 2147483647
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited = set()

        q = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if not grid[r][c]:
                    q.append((r, c))
                    visited.add((r, c))


        def addCell(r, c):
            if min(r, c) < 0 or r >= ROWS or c >= COLS or (r, c) in visited or grid[r][c] == -1:
                return 
            visited.add((r, c))
            q.append((r, c))

        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                for dr, dc in directions:
                    addCell(r + dr, c + dc)
            dist += 1