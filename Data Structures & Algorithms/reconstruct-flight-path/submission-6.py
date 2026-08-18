class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        map = defaultdict(list)
        for u, v in sorted(tickets, reverse=True):
            map[u].append(v)
        
        res = []
        def dfs(s):
            while map[s]:
                d = map[s].pop()
                dfs(d)
            res.append(s)
        
        dfs("JFK")
        return res[::-1]