"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x: x.start)
        for i in range(len(intervals) - 1):
            interval = intervals[i]
            nInterval = intervals[i + 1]
            cs, ce, ns, ne = interval.start, interval.end, nInterval.start, nInterval.end
            if ns < ce:
                return False
        return True

