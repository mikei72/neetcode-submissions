class TimeMap:

    def __init__(self):
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map:
            self.map[key] = {}
        self.map[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ""
        
        times = sorted(self.map[key].keys())
        l, r = 0, len(times) - 1
        time = -1

        while l <= r:
            mid = (l + r) // 2
            if timestamp > times[mid]:
                l = mid + 1
                time = max(time, times[mid])
            elif timestamp < times[mid]:
                r = mid - 1
            else:
                return self.map[key][times[mid]]
        
        if time != -1:
            return self.map[key][time]
        else:
            return ""
