class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        R = len(grid)
        C = len(grid[0])
        INF = 2147483647
        q = deque()
        visited = set()
        dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))

        for r in range(R):
            for c in range(C):
                if grid[r][c] == 0:
                    q.append((r, c, 0))
                    visited.add((r, c))
        
        while q:
            r, c, cur = q.popleft()
            for dr, dc in dirs:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < R and 0 <= nc < C and (nr, nc) not in visited and grid[nr][nc] != -1:
                    grid[nr][nc] = cur + 1
                    visited.add((nr, nc))
                    q.append((nr, nc, cur + 1))
