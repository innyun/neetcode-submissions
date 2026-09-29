class Solution:
    def partition(self, s: str) -> List[List[str]]:
        substrings = []

        def isPalindrome(s, i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        def backtrack(i, j, cur):
            if j >= len(s):
                if i == j:
                    substrings.append(cur.copy())
                return
            
            if isPalindrome(s, i, j):
                cur.append(s[i : j + 1])
                backtrack(j + 1, j + 1, cur)
                cur.pop()
            
            backtrack(i, j + 1, cur)

        backtrack(0, 0, [])
        
        return substrings

