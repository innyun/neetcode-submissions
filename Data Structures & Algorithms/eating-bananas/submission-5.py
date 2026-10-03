class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        b = max(piles)
        a = 1

        while a <= b:
            th = h
            m = (a + b) // 2
            done = False
            for p in piles:
                th -= (p + m - 1) // m
                if th < 0: 
                    break
            if th >= 0:
                done = True
            if done:
                b = m - 1
            else:
                a = m + 1

        return a