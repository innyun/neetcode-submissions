class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]

        s, e = intervals[0]
        ns, ne = newInterval

        i = 0
        while ns > e:
            i += 1
            if i > len(intervals) - 1:
                break
            s, e = intervals[i]

        intervals.insert(i, newInterval)

        print(intervals)

        while i + 1 < len(intervals):
            action = False
            if intervals[i + 1][0] <= intervals[i][0]:
                intervals[i][0] = intervals[i + 1][0]
                action = True
            if intervals[i + 1][0] <= intervals[i][1]:
                intervals[i][1] = max(intervals[i + 1][1], intervals[i][1])
                action = True
            if not action:
                break
            intervals.pop(i + 1)

        return intervals