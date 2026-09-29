class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        m = 0

        chars = {}
        a, b = 0, 0

        while b < len(s):
            if s[b] in chars:
                a = max(a, chars[s[b]] + 1)
                del(chars[s[b]])
            chars[s[b]] = b
            b += 1
            m = max(b - a, m)   

        return m 

