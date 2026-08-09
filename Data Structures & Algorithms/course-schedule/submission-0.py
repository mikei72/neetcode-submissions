class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        map = {i : [] for i in range(numCourses)}
        for course, pre in prerequisites:
            map[course].append(pre)
        
        visited = set()

        def dfs(crs):
            if crs in visited:
                return False
            if not map[crs]:
                return True

            visited.add(crs)
            for pre in map[crs]:
                if not dfs(pre):
                    return False
            visited.remove(crs)

            map[crs] = []

            return True


        for i in range(numCourses):
            if not dfs(i):
                return False
        return True