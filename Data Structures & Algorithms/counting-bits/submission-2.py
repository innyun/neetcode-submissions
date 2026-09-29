class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        out = [0, 1]
        for i in range(2, n + 1):
            out.append(out[i // 2] + (i & 1))
        return out
