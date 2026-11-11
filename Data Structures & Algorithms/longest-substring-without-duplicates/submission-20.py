class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        m = 0
        l = len(s)
        seen = {}

        a, b = 0, 0
        while b < l:
            if s[b] in seen:
                a = max(seen[s[b]] + 1, a)
            seen[s[b]] = b
            m = max(m, b - a + 1)
            b += 1

        return m