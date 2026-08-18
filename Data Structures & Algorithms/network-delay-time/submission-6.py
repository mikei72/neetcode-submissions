class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dist = [float("inf")] * (n + 1)
        dist[k] = 0

        map = defaultdict(list)
        for u, v, t in times:
            map[u].append([v, t])
        
        q = deque([(k, 0)])

        while q:
            node, time = q.popleft()
            if dist[node] < time:
                continue
            
            for nei, t in map[node]:
                if time + t < dist[nei]:
                    dist[nei] = time + t
                    q.append((nei, dist[nei]))

        res = max(dist[1:])
        return res if res < float("inf") else -1