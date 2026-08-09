class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        connect = [0] * numCourses
        adj = [[] for _ in range(numCourses)]
        for start, end in prerequisites:
            connect[start] += 1
            adj[end].append(start)
        
        res = []
        q = deque()
        for i in range(numCourses):
            if not connect[i]:
                q.append(i)
                res.append(i)
        
        while q:
            node = q.popleft()
            
            for n in adj[node]:
                connect[n] -= 1
                if not connect[n]:
                    q.append(n)
                    res.append(n)
        
        return res if len(res) == numCourses else []