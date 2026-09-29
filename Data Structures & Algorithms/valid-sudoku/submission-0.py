class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seenh = set()
        seenv = set()
        for i in range(9):
            for j in range(9):
                if board[i][j] in seenh:
                    print(seenh)
                    return False
                if board[j][i] in seenv:
                    print(seenv)
                    return False
                if board[i][j] != '.':
                    seenh.add(board[i][j])
                if board[j][i] != '.':
                    seenv.add(board[j][i])

            seenh = set()
            seenv = set()
        seens = set()
        offsetx = 0
        offesty = 0
        for offsetx in range(0, 7, 3):
            for offsety in range(0, 7, 3):
                for i in range(3):
                    for j in range(3):
                        if board[i + offsety][j + offsetx] in seens:
                            return False
                        if board[i + offsety][j + offsetx] != '.':
                            seens.add(board[i + offsety][j + offsetx])
                seens = set()

        return True