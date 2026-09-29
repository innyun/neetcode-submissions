class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        out = x
        for _ in range(abs(n) - 1):
            out *= x
        return out if n > 0 else 1 / out
