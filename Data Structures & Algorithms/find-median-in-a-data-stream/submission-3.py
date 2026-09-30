class MedianFinder:

    def __init__(self):
        self.h = []
        self.mh = []
        self.l = 0
        self.lh = 0

    def addNum(self, num: int) -> None:
        # print(self.h, self.l, self.lh, self.mh)
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
        if self.lh == 1:
            return self.h[0]
        elif self.l % 2 == 1:
            return self.h[0]
        else:
            v1 = self.h[0]
            heapq.heappop(self.h)
            v2 = self.h[0]
            heapq.heappush(self.h, v1)
            return (v1 + v2) / 2
        