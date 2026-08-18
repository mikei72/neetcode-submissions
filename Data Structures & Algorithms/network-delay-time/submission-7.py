class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        map = defaultdict(list)
        for u, v, t in times:
            map[u].append((v, t))
        
        visited = set()
        time = 0
        heap =[(0, k)]

        while heap:
            t1, n1 = heapq.heappop(heap)
            if n1 in visited:
                continue
            visited.add(n1)
            time = t1

            for n2, t2 in map[n1]:
                if n2 not in visited:
                    heapq.heappush(heap, (t1 + t2, n2))
        
        return time if len(visited) == n else -1