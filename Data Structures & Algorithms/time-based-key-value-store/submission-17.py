class TimeMap:

    def __init__(self):
        self.map = {}
        self.times  = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map:
            self.map[key] = []
        self.map[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        values = self.map.get(key, [])
        l, r = 0, len(values) - 1
        res = ""

        while l <= r:
            mid = (l + r) // 2
            if timestamp >= values[mid][0]:
                l = mid + 1
                res = values[mid][1]
            elif timestamp < values[mid][0]:
                r = mid - 1
        
        return res
