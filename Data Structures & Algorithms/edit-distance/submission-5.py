class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {}
        
        def recurse(i, j):
            if i == len(word1):
                return len(word2) - j
            if j == len(word2):
                return len(word1) - i
            
            if (i, j) in memo:
                return memo[(i, j)]

            if word1[i] == word2[j]:
                result = recurse(i + 1, j + 1)
                memo[(i, j)] = result
                return result

            result = min(1 + recurse(i + 1, j), 1 + recurse(i, j + 1), 1 + recurse(i + 1, j + 1))
            memo[(i, j)] = result
            return result
        
        return recurse(0, 0)
        

