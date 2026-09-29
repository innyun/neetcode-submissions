class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = (1 << 31) -1
        INT_MIN = -(1 << 31)
        negative = False

        out = 0
        if x < 0:
            negative = True
        x = abs(x)
        while x:
            out *= 10
            d = x % 10
            out += d
            x //= 10
        if negative:
            out = -out
        return int(out) if INT_MIN <= out <= INT_MAX else 0
