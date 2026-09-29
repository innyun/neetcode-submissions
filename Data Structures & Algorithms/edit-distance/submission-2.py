class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {}

        def recurse(i, j, n):
            if (i, j, n) in memo:
                return memo[(i, j, n)]
            if i == len(word1) and j == len(word2):
                return n
            if i == len(word1):
                return n + len(word2) - j
            if j == len(word2):
                return n + len(word1) - i
            if word1[i] == word2[j]:
                m = recurse(i + 1, j + 1, n)
            else:
                m = min(recurse(i, j + 1, n + 1), recurse(i + 1, j, n + 1), recurse(i + 1, j + 1, n + 1))
            memo[(i, j, n)] = m
            return m 
                

        return recurse(0, 0, 0)