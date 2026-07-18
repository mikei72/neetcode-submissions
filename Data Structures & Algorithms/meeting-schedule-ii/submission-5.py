"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0

        intervals.sort(key = lambda x: x.start)
        rooms = [intervals[0].end]

        for i in range(1, len(intervals)):
            hasRoom = False
            for j in range(len(rooms)):
                if intervals[i].start >= rooms[j]:
                    hasRoom = True
                    rooms[j] = intervals[i].end
                    break
            if not hasRoom:
                rooms.append(intervals[i].end)

        return len(rooms)