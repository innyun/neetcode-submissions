class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        newIntervals = []
        s, e = newInterval
        i = 0
        while i < len(intervals) and intervals[i][1] < s:
            start, end = intervals[i]
            if end < s:
                newIntervals.append([start, end])
                i += 1
            else:
                break
        while i < len(intervals) and e >= intervals[i][0]:
            if intervals[i][0] < s:
                s = intervals[i][0]
            if intervals[i][1] > e:
                e = intervals[i][1]
            i += 1
        newIntervals.append([s, e])
        newIntervals.extend(intervals[i:])

        return newIntervals
            