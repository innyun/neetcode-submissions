class Solution:
    def numDecodings(self, s: str) -> int:
        decodings = 0
        l = len(s)

        def search(cs, start):
            nonlocal decodings
            if start >= l:
                decodings += 1
                return
            if start == l - 1: 
                if s[-1] != '0':
                    search(cs, start + 1)
                return
            if cs[start:start+2] >= '10' and cs[start:start+2] <= '26':
                search(cs, start + 2)
            if cs[start] != '0':
                search(cs, start + 1)

        search(s, 0)
        return decodings