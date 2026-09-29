class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        parentheses = []

        def backtrack(cur, pairs, remaining):
            if remaining == 0 and not pairs:
                parentheses.append(cur)
                return
            
            if pairs and pairs[-1] == '(':
                cur += ')'
                pairs = pairs[:-1]
                backtrack(cur, pairs, remaining)
                cur = cur[:-1]
                pairs += '('
            if remaining > 0:
                cur += '('
                pairs += '('
                backtrack(cur, pairs, remaining - 1)

        backtrack('', '', n)    

        return parentheses
