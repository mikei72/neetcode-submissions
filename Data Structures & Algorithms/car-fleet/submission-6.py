class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        times = set()

        paired = sorted(zip(position, speed), reverse=True)
        max_t = 0

        for pos, v in paired:
            t = (target - pos) / v
            if t > max_t:
                times.add(t)
                max_t = t

        return len(times)