class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        st = []

        for l in s:
            if l in mapping:
                if not st or mapping[l] != st.pop():
                    return False
            else:
                st.append(l)
        
        return len(st) == 0