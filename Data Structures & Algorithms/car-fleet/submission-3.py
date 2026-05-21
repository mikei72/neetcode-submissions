class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        times = set()

        paired = sorted(zip(position, speed), reverse=True)
        position, speed = zip(*paired)
        position, speed = list(position), list(speed)

        max_t = 0

        for i in range(len(position)):
            t = (target - position[i]) / speed[i]
            if t > max_t:
                times.add(t)
                max_t = t

        return len(times)