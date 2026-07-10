class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks).most_common()
        maxf = count[0][1]
        
        idle = (maxf - 1) * n

        for i in range(len(count) - 1):
            idle -= min(maxf - 1, count[i + 1][1])

        return len(tasks) + max(0, idle)
