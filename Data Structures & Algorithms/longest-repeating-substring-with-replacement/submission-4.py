class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        a = 0
        b = 0
        count = defaultdict(int)
        maxCount = 0
        longest = 0
        while b < len(s):
            count[s[b]] += 1
            maxCount = max(maxCount, count[s[b]])

            while b - a + 1 - maxCount > k:
                count[s[a]] -= 1
                a += 1

            longest = max(longest, b - a + 1)

            b += 1
        return longest