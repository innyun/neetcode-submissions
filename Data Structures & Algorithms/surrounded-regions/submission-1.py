class Solution:
    def solve(self, board: List[List[str]]) -> None:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        def dfs(i, j):
            for direction in directions:
                ni, nj = i + direction[0], j + direction[1]
                if 0 <= ni < len(board) and 0 <= nj < len(board[0]) and board[ni][nj] == 'O':
                    board[ni][nj] = 'M'
                    dfs(ni, nj)
        
        for x in range(len(board)):
            dfs(x, -1)
            dfs(x, len(board[0]))
        for y in range(len(board[0])):
            dfs(-1, y)
            dfs(len(board), y)

        print(board)

        for x in range(len(board)):
            for y in range(len(board[0])):
                if board[x][y] == 'O':
                    board[x][y] = 'X'
                elif board[x][y] == 'M':
                    board[x][y] = 'O'