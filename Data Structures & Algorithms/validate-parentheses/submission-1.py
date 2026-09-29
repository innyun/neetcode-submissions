class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        d = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        for p in s:
            if p in d:
                if not st or d[p] != st.pop():
                    return False
            else:
                st.append(p)
        return not st