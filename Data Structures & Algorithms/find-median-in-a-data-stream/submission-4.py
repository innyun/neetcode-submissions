class MedianFinder:

    def __init__(self):
        self.h = []
        self.mh = []
        self.l = 0
        self.lh = 0

    def addNum(self, num: int) -> None:
        self.l += 1
        if not self.h or (self.lh < self.l // 2 + 1):
            heapq.heappush(self.mh, -num)
            heapq.heappush(self.h, -heapq.heappop(self.mh))
            self.lh += 1
        elif self.h[0] < num:
            heapq.heappush(self.mh, -num)
            v = heapq.heappop(self.h)
            heapq.heappush(self.h, -heapq.heappop(self.mh))
            heapq.heappush(self.mh, -v)
        else:
            heapq.heappush(self.mh, -num)

    def findMedian(self) -> float:
        h = self.h

        if self.l & 1:
            return h[0]

        a = h[0]
        b = h[1] if len(h) == 2 else min(h[1], h[2])
        return (a + b) / 2