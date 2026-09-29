class Solution:
    def getSum(self, a: int, b: int) -> int:
        c = 0
        carry = 0

        for i in range(32):
            bit1 = (a >> i) & 1
            bit2 = (b >> i) & 1

            bit = bit1 ^ bit2 ^ carry

            c = (bit << i) | c

            carry = carry & bit1 | carry & bit2 | bit1 & bit2

        if c > 0x7FFFFFFF:
            c = ~(c ^ 0xFFFFFFFF)

        return c
