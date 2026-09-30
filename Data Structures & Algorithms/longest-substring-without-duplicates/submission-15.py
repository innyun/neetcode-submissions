class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        longest = 0
        a = 0

        for b, c in enumerate(s): 
            if c in seen: 
                a = max(seen[c] + 1, a)
            longest = max(longest, b - a + 1)
            seen[c] = b


        return longest
