class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0

        R = len(grid)
        C = len(grid[0])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def bfs(r, c):
            q = deque([(r, c)])

            while q:
                r, c = q.popleft()
                if 0 <= r < R and 0 <= c < C and grid[r][c] == "1":
                    grid[r][c] = "0"
                    for dr, dc in dirs:
                        q.append((r + dr, c + dc))

        for r in range(R):
            for c in range(C):
                if grid[r][c] == "1":
                    bfs(r, c)
                    res += 1
        
        return res