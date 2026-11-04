class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort(key=lambda x: len(x))

        lo = strs[0]
        m = len(lo)
        for s in strs[1:]:
            i = 0
            while i < len(lo):
                if lo[i] != s[i]:
                    m = i
                    lo = lo[:m]
                i += 1
        
        return lo

        
            