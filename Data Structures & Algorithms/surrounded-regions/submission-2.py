class Solution:
    def solve(self, board: List[List[str]]) -> None:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        def dfs(i, j):
            if board[i][j] == 'O':
                board[i][j] = 'M'
                for direction in directions:
                    ni, nj = i + direction[0], j + direction[1]
                    if 0 <= ni < len(board) and 0 <= nj < len(board[0]) and board[ni][nj] == 'O':
                        dfs(ni, nj)
        
        for x in range(len(board)):
            dfs(x, 0)
            dfs(x, len(board[0]) - 1)
        for y in range(len(board[0])):
            dfs(0, y)
            dfs(len(board) - 1, y)

        for x in range(len(board)):
            for y in range(len(board[0])):
                if board[x][y] == 'O':
                    board[x][y] = 'X'
                elif board[x][y] == 'M':
                    board[x][y] = 'O'