class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        l1 = len(s1)
        l2 = len(s2)
        l3 = len(s3)

        memo = {}
        
        if l1 + l2 != l3:
            return False

        def recurse(i, j, k):
            if (i, j, k) in memo:
                return memo[(i, j, k)]
            if k == l3:
                return True
            m = False
            if i < l1 and s1[i] == s3[k]:
                m = recurse(i + 1, j, k + 1) or m
            if j < l2 and s2[j] == s3[k]:
                m = recurse(i, j + 1, k + 1) or m
            memo[(i, j, k)] = m
            return m
        
        return recurse(0, 0, 0)


            