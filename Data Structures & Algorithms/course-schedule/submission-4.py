class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        connect = [0] * numCourses
        adj = [[] for _ in range(numCourses)]
        for start, end in prerequisites:
            connect[end] += 1
            adj[start].append(end)
        
        q = deque()
        for i in range(numCourses):
            if not connect[i]:
                q.append(i)
        
        finish = 0
        while q:
            node = q.popleft()
            finish += 1
            
            for n in adj[node]:
                connect[n] -= 1
                if not connect[n]:
                    q.append(n)
        
        return finish == numCourses