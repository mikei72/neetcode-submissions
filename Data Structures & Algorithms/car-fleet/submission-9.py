class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        times = set()

        paired = sorted(zip(position, speed), reverse=True)
        max_t = 0

        for i in range(len(paired)):
            t = (target - paired[i][0]) / paired[i][1]
            if t > max_t:
                times.add(t)
                max_t = t

        return len(times)