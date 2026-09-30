class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        closest = []

        for x, y in points: 
            d = -(x**2 + y**2)
            if k > 0:   
                heapq.heappush(closest, (d, x, y))
                k -= 1
            elif d >= closest[0][0]:
                heapq.heappushpop(closest, (d, x, y))

        return [[x, y] for _, x, y in closest]
