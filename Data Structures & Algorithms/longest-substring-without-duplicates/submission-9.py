class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        m = 0

        chars = set()
        a, b = 0, 0

        while b < len(s): 
            if s[b] not in chars:
                chars.add(s[b])
                b += 1
                m = max(b - a, m)   
            else: 
                while s[a] != s[b]:
                    chars.remove(s[a])
                    a += 1
                a += 1
                b += 1

        return m 

