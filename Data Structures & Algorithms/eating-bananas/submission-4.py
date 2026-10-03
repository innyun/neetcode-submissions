class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        b = max(piles)
        a = 1

        while a <= b:
            t = piles.copy()
            th = h
            m = (a + b) // 2
            done = False
            # print(a, b, m, th, t)
            for i in range(len(t)):
                th -= (math.ceil(t[i] / m))
                # print(t, th)
            if th >= 0:
                done = True
            if done:
                b = m - 1
            else:
                a = m + 1

        return a