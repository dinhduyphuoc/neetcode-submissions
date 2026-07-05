class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        l = 0
        r = rows * cols - 1

        while l <= r:
            pivot = (r + l) // 2
            row = pivot // cols
            col = pivot % cols
            if matrix[row][col] == target:
                return True
            if matrix[row][col] < target:
                l = pivot + 1
            else:
                r = pivot - 1
        
        return False