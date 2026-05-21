class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        paired = sorted(zip(position, speed), reverse=True)
        max_t = 0
        fleets = 0

        for i in range(len(paired)):
            t = (target - paired[i][0]) / paired[i][1]
            if t > max_t:
                fleets += 1
                max_t = t

        return fleets