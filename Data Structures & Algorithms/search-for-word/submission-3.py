class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        R = len(board)
        C = len(board[0])

        def dfs(curIdx, r, c):
            if curIdx == len(word):
                return True
            if r < 0 or r >= R or c < 0 or c >= C:
                return False
            if board[r][c] == "#" or board[r][c] != word[curIdx]:
                return False
            num = board[r][c]
            board[r][c] = "#"
            res = (dfs(curIdx + 1, r + 1, c) or
                    dfs(curIdx + 1, r - 1, c) or
                    dfs(curIdx + 1, r, c + 1) or
                    dfs(curIdx + 1, r, c - 1))
            board[r][c] = num
            return res

        for r in range(R):
            for c in range(C):
                if board[r][c] == word[0]:
                    if dfs(0, r, c):
                        return True
        
        return False