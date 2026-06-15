class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == ".":
                    continue
                boxNo = (i // 3) * 3 + (j // 3)
                if board[i][j] in cols[j] or board[i][j] in rows[i] or board[i][j] in boxes[boxNo]:
                    return False
                cols[j].add(board[i][j]) 
                rows[i].add(board[i][j])
                boxes[boxNo].add(board[i][j])
        return True