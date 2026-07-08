class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxStone = max(stones)
        bucket = [0] * (maxStone + 1)

        for stone in stones:
            bucket[stone] += 1

        x = y = maxStone
        while x > 0:
            if bucket[x] % 2 == 0:
                x -= 1
                continue
            
            j = min(x - 1, y)
            while j > 0 and bucket[j] == 0:
                j -= 1
            
            if j == 0:
                return x

            y = j
            bucket[x] -= 1
            bucket[y] -= 1
            bucket[x - y] += 1
            x = max(x - y, y)
        
        return x
