class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        heap = [-cnt for cnt in count.values()]
        heapq.heapify(heap)

        cycle = 0
        q = deque()
        while heap or q:
            cycle += 1

            if not heap:
                cycle = q[0][1]
            else:
                cnt = heapq.heappop(heap) + 1
                if cnt:
                    q.append([cnt, cycle + n])
                
            if q and q[0][1] == cycle:
                heapq.heappush(heap, q.popleft()[0])
        
        return cycle

