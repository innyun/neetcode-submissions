class Solution:
    def validPalindrome(self, s: str) -> bool:
        a, b = 0, len(s) - 1
        c = True
        d = True
        while a < b:
            if s[a] != s[b]:
                if not c:
                    d = False
                c = False
                a += 1
            else:
                a += 1
                b -= 1
        a, b = 0, len(s) - 1
        c = True
        while a < b:
            if s[a] != s[b]:
                if not c:
                    if not d:
                        return False
                c = False
                b -= 1
            else:
                a += 1
                b -= 1
        return True