class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        cur = []
        stack = []

        def backtrack(remaining):
            if remaining == 0 and not stack:
                res.append("".join(cur))
                return

            if stack:  # close
                cur.append(')')
                stack.pop()
                backtrack(remaining)
                stack.append('(')
                cur.pop()

            if remaining > 0:  # open
                cur.append('(')
                stack.append('(')
                backtrack(remaining - 1)
                stack.pop()
                cur.pop()

        backtrack(n)
        return res
