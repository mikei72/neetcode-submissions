class TimeMap:

    def __init__(self):
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map:
            self.map[key] = []
        self.map[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.map.get(key, [])
        
        l, r = 0, len(values) - 1

        while l <= r:
            mid = (l + r) // 2
            if timestamp >= values[mid][0]:
                res = values[mid][1]
                l = mid + 1
            else:
                r = mid - 1
        
        return res
