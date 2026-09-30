"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        ends = []
        intervals.sort(key=lambda x: x.start)

        for interval in intervals:
            if not ends: 
                heapq.heappush(ends, interval.end)
            else:  
                if interval.start >= ends[0]:
                    heapq.heappop(ends)
                heapq.heappush(ends, interval.end)
                
        return len(ends)