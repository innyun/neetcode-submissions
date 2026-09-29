class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        longest = 0
        a, b = 0, 0
        while b < len(s):
            if s[b] in seen:
                longest = max(longest, b - a)
                if seen[s[b]] >= a:
                    a = seen[s[b]] + 1
            seen[s[b]] = b
            b += 1
        return max(longest, b-a)