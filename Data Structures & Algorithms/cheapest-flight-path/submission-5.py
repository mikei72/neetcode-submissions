class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        map = defaultdict(list)
        for s, d, p in flights:
            map[s].append((d, p))

        prices = [float("inf")] * n
        prices[src] = 0

        q = deque([(0, src, 0)])
        while q:
            p, node, stops = q.popleft()
            if stops > k:
                break
            
            for nei, cst in map[node]:
                nextCst = cst + p
                if nextCst < prices[nei]:
                    prices[nei] = nextCst
                    q.append((nextCst, nei, stops + 1))
        
        return prices[dst] if prices[dst] != float("inf") else -1