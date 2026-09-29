class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        x = len(board)
        y = len(board[0])
        found = False
        def backtrack(i, j, cur):
            nonlocal found
            if found:
                return

            if cur == len(word):
                found = True
                return

            for direction in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                i += direction[0]
                j += direction[1]
                if i < 0 or i >= x or j < 0 or j >= y or not board[i][j]:
                    i -= direction[0]
                    j -= direction[1]
                    continue
                if board[i][j] == word[cur]:
                    board[i][j] = ''
                    backtrack(i, j, cur + 1)
                    board[i][j] = word[cur]
                i -= direction[0]
                j -= direction[1]
        
        for i in range(x):
            for j in range(y):
                if board[i][j] == word[0]:
                    board[i][j] = ''
                    backtrack(i, j, 1)
                    board[i][j] = word[0]

        return found