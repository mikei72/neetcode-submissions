class TimeMap:

    def __init__(self):
        self.map = {}
        self.times  = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map:
            self.map[key] = {}
            self.times[key] = []
        self.map[key][timestamp] = value
        self.times[key].append(timestamp)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ""
        
        times = self.times[key]
        l, r = 0, len(times) - 1
        res = ""

        while l <= r:
            mid = (l + r) // 2
            if timestamp >= times[mid]:
                l = mid + 1
                res = self.map[key][times[mid]]
            elif timestamp < times[mid]:
                r = mid - 1
        
        return res
