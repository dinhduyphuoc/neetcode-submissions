class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        
        for R in range(9):
            for C in range(9):
                if board[R][C] == '.':
                    continue
                boxIdx = (R // 3) * 3 + (C // 3) 
                if board[R][C] in rows[R] or board[R][C] in cols[C] or board[R][C] in boxes[boxIdx]:
                    return False
                rows[R].add(board[R][C])
                cols[C].add(board[R][C])
                boxes[boxIdx].add(board[R][C])
        return True