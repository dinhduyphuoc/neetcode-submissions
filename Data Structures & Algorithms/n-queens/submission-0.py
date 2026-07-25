class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [["."] * n for _ in range(n)]
        checkC = [True] * n
        checkD1 = [True] * (n*2-1)
        checkD2 = [True] * (n*2-1)

        def safe(r, c):
            if checkC[c] and checkD1[r + c] and checkD2[r - c + (n - 1)]:
                return True
            return False

        def setState(state, r, c):
            checkC[c] = state
            checkD1[r + c] = state
            checkD2[r - c + (n - 1)] = state

        def backtrack(r):
            if r >= n:
                res.append(["".join(board[i]) for i in range(len(board))])
                return
            for c in range(n):
                if safe(r, c):
                    board[r][c] = "Q"
                    setState(False, r, c)
                    backtrack(r + 1)
                    board[r][c] = "."
                    setState(True, r, c)

        backtrack(0)
        return res