class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        newIntervals = []

        i = 0

        cs, ce = intervals[i]

        while i < len(intervals) - 1:
            ns, ne = intervals[i + 1]

            if ns <= ce:
                ce = max(ne, ce)
                i += 1
            elif ns > ce:
                newIntervals.append([cs, ce])
                i += 1
                cs, ce = intervals[i]
        
        if [cs, ce] not in newIntervals: 
            newIntervals.append([cs, ce])
        else:
            newIntervals.append(intervals[i])

        return newIntervals
