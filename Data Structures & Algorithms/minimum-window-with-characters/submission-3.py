class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        m = ""
        ml = float('inf')

        c = Counter(t)
        missing = len(t)

        a, b = 0, 0

        while b < len(s):
            if s[b] in c:
                if c[s[b]] > 0:
                    missing -= 1
                c[s[b]] -= 1
            while missing == 0:
                if b - a + 1 < ml:
                    ml = b - a + 1
                    m = s[a:b + 1]
                if s[a] in c:
                    c[s[a]] += 1
                    if c[s[a]] > 0:
                        missing += 1
                a += 1
            b += 1

        return m