class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        c = Counter(s1)
        l = len(s1)
        a = 0
        for b in range(len(s2)):
            if s2[b] in c and c[s2[b]] > 0:
                c[s2[b]] -= 1
            else:
                while s2[a] != s2[b]:
                    if s2[a] in c:
                        c[s2[a]] += 1
                    a += 1
                a += 1
            if b - a + 1 == l:
                return True
        return False
