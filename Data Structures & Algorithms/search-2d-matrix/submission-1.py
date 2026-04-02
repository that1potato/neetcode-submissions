class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]: return False
        rows, cols = len(matrix), len(matrix[0])
        
        top, bot = 0, rows - 1
        target_row = -1
        
        while top <= bot:
            mid = (top + bot) // 2
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                target_row = mid
                break 
            elif matrix[mid][0] > target:
                bot = mid - 1
            else:
                top = mid + 1
        
        if target_row == -1:
            return False

        l, r = 0, cols - 1
        while l <= r:
            mid = (l + r) // 2
            if matrix[target_row][mid] == target:
                return True
            elif matrix[target_row][mid] > target:
                r = mid - 1
            else:
                l = mid + 1
                
        return False