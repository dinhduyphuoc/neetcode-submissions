class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binarysearch(i, l, r):
            while l <= r:
                pivot = (l + r) // 2
                if matrix[i][pivot] == target:
                    return True
                if matrix[i][pivot] < target:
                    l = pivot + 1
                else:
                    r = pivot - 1
            return False
        
        l = 0
        r = len(matrix) - 1

        while l <= r:
            pivot = (l + r) // 2
            if matrix[pivot][0] == target:
                return True
            if matrix[pivot][0] > target:
                r = pivot - 1
            else:
                rtemp = len(matrix[0]) - 1
                if matrix[pivot][0] < target <= matrix[pivot][rtemp]:
                    return binarysearch(pivot, 0, rtemp)
                else:
                    l = pivot + 1

        return False