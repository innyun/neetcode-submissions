class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)
        for n in nums:
            d[n] += 1
        h = []
        for key, value in d.items():
            heapq.heappush(h, (-value, key))
        out = []
        for _ in range(k):
            out.append(heapq.heappop(h)[1])
        return out
