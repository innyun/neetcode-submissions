class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        a = 0
        b = len(matrix) - 1

        while a < b:
            m = (a + b) // 2
            if matrix[m][-1] == target:
                return True
            elif matrix[m][-1] > target:
                b = m
            else:
                a = m + 1 
        
        c = 0
        d = len(matrix[0]) - 1

        while c <= d:
            m = (c + d) // 2
            if matrix[a][m] == target:
                return True
            elif matrix[a][m] > target:
                d = m - 1
            else:
                c = m + 1
        
        return False
