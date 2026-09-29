class Solution:
    def isPalindrome(self, s: str) -> bool:
        a = 0
        b = len(s) - 1
        while a < b:
            if not s[a].isalnum():
                a += 1
            elif not s[b].isalnum():
                b -= 1
            elif s[a].lower() != s[b].lower():
                return False
            else:
                a += 1
                b -= 1
        return True