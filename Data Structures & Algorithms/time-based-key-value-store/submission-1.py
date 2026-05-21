class TimeMap:

    def __init__(self):
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map:
            self.map[key] = {}
        if timestamp not in self.map[key]:
            self.map[key][timestamp] = []
        self.map[key][timestamp].append(value)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ""
        
        time = -1
        for t in self.map[key]:
            if t <= timestamp:
                time = max(time, t)

        if time != -1:
            return self.map[key][time][-1]
        else:
            return ""
