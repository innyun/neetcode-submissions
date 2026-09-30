class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        newIntervals = []
        intervals.sort()

        cs, ce = intervals[0]
        for i in range(len(intervals) - 1):
            ns, ne = intervals[i + 1]
            if ns <= ce:
                ce = max(ce, ne)
            else:
                newIntervals.append([cs, ce])
                i += 1
                cs, ce = intervals[i]
        newIntervals.append([cs, ce])
        

        return newIntervals