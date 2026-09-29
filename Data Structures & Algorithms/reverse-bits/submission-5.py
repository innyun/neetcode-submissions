class Solution:
    def reverseBits(self, n: int) -> int:
        out = 0
        for _ in range(32):
            out <<= 1
            bit = n & 1
            out = out | bit
            n >>= 1
        return out