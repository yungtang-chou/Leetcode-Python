## Useful Reference: 
## https://leetcode.com/problems/set-matrix-zeroes/discuss/657430/Python-Solution-w-approach-explanation-and-readable-with-space-progression-from%3A-O(m%2Bn)-and-O(1)


## Space O(m+n)
## Keep lists of flags and then update based on the flag
# Runtime: 124 ms, faster than 92.26% of Python3 online submissions for Set Matrix Zeroes.
# Memory Usage: 15.1 MB, less than 73.88% of Python3 online submissions for Set Matrix Zeroes.

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        if not matrix:
            return []
        
        m = len(matrix)
        n = len(matrix[0])
        
        ## record flags for all rows and columns
        zeroes_row = [False] * m
        zeroes_col = [False] * n
        
        ## loop through all cells and keep track of the flag
        for row in range(m):
            for col in range(n):
                if matrix[row][col] == 0:
                    zeroes_row[row] = True
                    zeroes_col[col] = True
                    
        ## update based on the flags
        for row in range(m):
            for col in range(n):
                if zeroes_row[row] or zeroes_col[col]:
                    matrix[row][col] = 0


## Space O(1)
## Use the first column and first row as flags instead of using additional space
# Runtime: 132 ms, faster than 64.39% of Python3 online submissions for Set Matrix Zeroes.
# Memory Usage: 15.2 MB, less than 46.17% of Python3 online submissions for Set Matrix Zeroes.

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        m, n = len(matrix), len(matrix[0])
        zero_row, zero_column = False, False
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    ## mark its first row/ column as zero
                    matrix[i][0] = matrix[0][j] = 0
                    zero_row = True if i == 0 else zero_row
                    zero_column = True if j == 0 else zero_column
        
        ## update each cell if its first column / first cell is zero
        for i in range(1, m):
            for j in range(1, n):
                matrix[i][j] = 0 if matrix[0][j] == 0 or matrix[i][0] == 0 else matrix[i][j]
        
        ## check the flag and update its first row
        if zero_row:
            for j in range(n):
                matrix[0][j] = 0
                
        ## check the flag and update its first column
        if zero_column:
            for i in range(m):
                matrix[i][0] = 0