class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = s[0]
        llongest = 1
        l = len(s)
        for i in range(l):
            a, b = i, i
            while a >= 0 and b < l and s[a] == s[b]:
                if b - a + 1> llongest:
                    llongest = b - a + 1
                    longest = s[a:b+1]
                a -= 1
                b += 1
            if i < l - 1:
                a, b = i, i + 1
                while a >= 0 and b < l and s[a] == s[b]:
                    if b - a + 1> llongest:
                        llongest = b - a + 1
                        longest = s[a:b+1]
                    a -= 1
                    b += 1
        return longest

