class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for string in strs:
            encoded_string += str(len(string)) + "#"
            encoded_string += string
        return encoded_string

    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0
        n = ''
        temp = ''
        while i < len(s):
            while s[i] != '#':
                n += s[i]
                i += 1
            i += 1
            n = int(n)
            for _ in range(n):
                temp += s[i]
                i += 1
            strs.append(temp)
            temp = ''
            n = ''
        return strs