class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        missing = len(t)
        d = Counter(t)

        a = 0

        shortest = ""
        ls = float("inf")

        for b, c in enumerate(s):
            if c in d:
                if d[c] > 0:
                    missing -= 1
                d[c] -= 1
            while missing == 0:
                if b - a + 1 < ls:
                    ls = b - a + 1
                    shortest = s[a:b + 1]
                if s[a] in d:
                    d[s[a]] += 1
                    if d[s[a]] > 0:
                        missing += 1
                a += 1


        return shortest