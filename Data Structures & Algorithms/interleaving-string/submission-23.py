class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        memo = {} 

        def recurse(i, j, k):
            if i == len(s1):
                return s3[k:] == s2[j:]
            if j == len(s2):
                return s3[k:] == s1[i:]
            if k == len(s3):
                return False

            if (i, j, k) in memo:
                return memo[(i, j, k)]
            
            result1 = False
            result2 = False
            if s1[i] == s3[k]:
                result1 = recurse(i + 1, j, k + 1)

            if s2[j] == s3[k]:
                result2 = recurse(i, j + 1, k + 1)

            memo[(i, j, k)] = result1 or result2
            return result1 or result2

            return False

        return recurse(0, 0, 0)
