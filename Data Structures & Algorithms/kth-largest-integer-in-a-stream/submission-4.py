class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.l = 0
        self.h = []
        for n in nums:
            if self.l < self.k:
                heapq.heappush(self.h, n)
                self.l += 1
            elif self.h[0] < n:
                heapq.heappushpop(self.h, n)

    def add(self, val: int) -> int:
        if self.l < self.k:
            heapq.heappush(self.h, val)
            self.l += 1
        else:
            heapq.heappushpop(self.h, val)
        return self.h[0]



# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)