class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        R = len(grid)
        C = len(grid[0])
        visited = set()
        res = 0
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def bfs(r, c):
            q = deque([(r, c)])
            area = 0
            while q:
                r, c = q.popleft()
                if 0 <= r < R and 0 <= c < C and grid[r][c] == 1 and (r, c) not in visited:
                    area += 1
                    visited.add((r, c))
                    for dr, dc in dirs:
                        q.append((r + dr, c + dc))
            return area


        for r in range(R):
            for c in range(C):
                if (r, c) not in visited and grid[r][c] == 1:
                    res = max(res, bfs(r, c))
                    visited.add((r, c))
        
        return res