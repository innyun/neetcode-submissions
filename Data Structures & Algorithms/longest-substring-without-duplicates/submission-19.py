class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        m = 0
        l = len(s)
        seen = set()

        a, b = 0, 0
        while b < l:
            if s[b] in seen:
                while a < b and s[a] != s[b]:
                    seen.remove(s[a])
                    a += 1
                a += 1
            seen.add(s[b]) 
            m = max(m, b - a + 1)
            b += 1

        return m