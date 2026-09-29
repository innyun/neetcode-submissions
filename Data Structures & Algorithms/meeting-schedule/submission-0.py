"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key= lambda x: x.start)
        prev = None
        for interval in intervals:
            if prev and interval.start < prev:
                return False
            prev = interval.end
        return True

