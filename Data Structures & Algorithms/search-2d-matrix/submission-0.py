class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for m in matrix:
            l = 0
            r = len(m) - 1
            if target > m[r]:
                continue
            while l <= r:
                pivot = (l + r) // 2
                if m[pivot] == target:
                    return True
                if m[pivot] < target:
                    l = pivot + 1
                else:
                    r = pivot - 1

        return False