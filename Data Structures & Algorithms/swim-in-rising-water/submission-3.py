class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        time = 0
        heap = [[grid[0][0], 0, 0]]
        visited = set((0, 0))

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while heap:
            t, r, c = heapq.heappop(heap)

            if r == n - 1 and c == n - 1:
                return t

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (nr, nc) not in visited and min(nr, nc) >= 0 and max(nr, nc) < n:
                    visited.add((nr, nc))
                    heapq.heappush(heap, [max(t, grid[nr][nc]), nr, nc])
        
        return -1
