class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = defaultdict(int)
        for n in nums: 
            c[n] += 1
        
        h = []
        for key, value in c.items():
            heapq.heappush(h, [-value, key])

        r = []
        for _ in range(k):
            r.append(heapq.heappop(h)[1])
        return r