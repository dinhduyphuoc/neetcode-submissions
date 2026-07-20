class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        R = len(board)
        C = len(board[0])
        visited = set()
        found = False
        def backtrack(curIdx, r, c):
            if curIdx == len(word):
                nonlocal found
                found = True
                return 
            if 0 <= r < R and 0 <= c < C and (r, c) not in visited:
                if board[r][c] != word[curIdx]:
                    return 
                visited.add((r, c))
                backtrack(curIdx + 1, r + 1, c) 
                backtrack(curIdx + 1, r - 1, c) 
                backtrack(curIdx + 1, r, c + 1) 
                backtrack(curIdx + 1, r, c - 1) 
                visited.remove((r, c))

        for r in range(R):
            for c in range(C):
                if board[r][c] == word[0]:
                    backtrack(0, r, c)
                    if found:
                        return True
        
        return False