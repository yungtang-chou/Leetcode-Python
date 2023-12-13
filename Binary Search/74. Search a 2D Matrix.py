class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        rows, cols = len(matrix), len(matrix[0])

        top, bottom = 0, rows - 1

        ## check which row does the target possibly is in
        while top <= bottom:
            mid = (top+bottom)//2
            if target > matrix[mid][-1]:
                top = mid + 1
            elif target < matrix[mid][0]:
                bottom  = mid - 1
            else: ## it's in the mid row
                break  
        
        if not (top <= bottom):
            return False

        ## check if the number exists
        l, r = 0, cols - 1
        # mid = (top+bottom) // 2

        while l <= r:
            m = (l + r)//2
            if target > matrix[mid][m]:
                l = m + 1
            elif target < matrix[mid][m]:
                r = m - 1
            else:
                return True
        
        return False