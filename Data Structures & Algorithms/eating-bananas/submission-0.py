class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        minimum = float('inf')
        a, b = math.ceil(min(piles) / h), max(piles) 
        while a <= b:
            m = (a + b) // 2
            t = 0
            for p in piles:
                t += math.ceil(p / m)
            if t <= h:
                minimum = min(minimum, m)
                b = m - 1
            else:
                a = m + 1
        return minimum
            