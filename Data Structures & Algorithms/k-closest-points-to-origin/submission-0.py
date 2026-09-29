class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        closest = []
        heap = []
        for point in points:
            heapq.heappush(heap, ((point[0] * point[0] + point[1] * point[1]) ** (1/2), point))
        for _ in range(k):
            closest.append(heapq.heappop(heap)[1])
        return closest
