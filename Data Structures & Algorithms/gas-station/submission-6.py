class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        sub = [x - y for x, y in zip(gas, cost)]
        if sum(sub) < 0:
            return -1

        for station in range(len(sub)):
            if sub[station] >= 0:
                tank = sub[station]

                for i in range(len(sub) - 1):
                    tank += sub[(station + i + 1) % len(sub)]
                    if tank < 0:
                        break
                
                if tank >= 0:
                    return station
    
        return -1
