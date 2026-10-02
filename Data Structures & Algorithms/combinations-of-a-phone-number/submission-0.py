class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "": 
            return []

        self.mapping = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'], 
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'], 
            '6': ['m', 'n', 'o'], 
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        self.combos = []

        self.recurse("", digits)
        
        return self.combos
        
    def recurse(self, cur, digits):
        if not digits: 
            self.combos.append(cur)
            return
        for l in self.mapping[digits[0]]:
            self.recurse(cur + l, digits[1:])

    