class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lo = strs[0]
        for s in strs[1:]:
            while not s.startswith(lo):
                lo = lo[:-1]
        
        return lo

        
            