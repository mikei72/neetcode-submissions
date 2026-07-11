class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks).most_common()
        maxf = count[0][1]

        maxCount = 1
        for i in range(len(count) - 1):
            if count[i + 1][1] == maxf:
                maxCount += 1
            else:
                break
        
        return max(len(tasks), (maxf - 1) * (n + 1) + maxCount)
