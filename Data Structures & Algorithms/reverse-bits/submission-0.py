class Solution:
    def reverseBits(self, n: int) -> int:
        out = 0
        for i in range(31, -1, -1):
            if n & 1:
                out += 2**i
            n >>= 1
        return out