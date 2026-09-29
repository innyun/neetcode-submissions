class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        x = len(board)
        y = len(board[0])
        found = False
        def backtrack(i, j, remaining, visited):
            nonlocal found
            if found:
                return

            if not remaining:
                found = True
                return

            for direction in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                i += direction[0]
                j += direction[1]
                if i < 0 or i >= x or j < 0 or j >= y or (i, j) in visited:
                    i -= direction[0]
                    j -= direction[1]
                    continue
                if board[i][j] == remaining[0]:
                    visited.add((i, j))
                    backtrack(i, j, remaining[1:], visited)
                    visited.remove((i, j))
                i -= direction[0]
                j -= direction[1]
        
        for i in range(x):
            for j in range(y):
                if board[i][j] == word[0]:
                    backtrack(i, j, word[1:], {(i, j)})

        return found