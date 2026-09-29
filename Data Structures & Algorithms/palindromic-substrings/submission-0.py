class Solution:
    def countSubstrings(self, s: str) -> int:
        palindromes = 0
        l = len(s)

        for i in range(l):
            a, b = i, i
            while a >= 0 and b < l and s[a] == s[b]:
                palindromes += 1
                a -= 1
                b += 1
            if i + 1 < l:
                a, b = i, i + 1
                while a >= 0 and b < l and s[a] == s[b]:
                    palindromes += 1
                    a -= 1
                    b += 1
        
        return palindromes
                