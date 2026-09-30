class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        R = len(grid)
        C = len(grid[0])
        q = deque()
        total = 0
        time = -1
        visited = set()
        dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))
            
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 2:
                    q.append((r, c))
                    visited.add((r, c))
                elif grid[r][c] == 1:
                    total += 1
        if total == 0:
            return 0
        while q:
            for _ in range(len(q)):
                cr, cc = q.popleft()
                grid[cr][cc] = 2
                for dr, dc in dirs:
                    nr = cr + dr
                    nc = cc + dc
                    if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] == 1 and (nr, nc) not in visited:
                        q.append((nr, nc))
                        visited.add((nr, nc))
                        total -= 1
            time += 1
        return time if total == 0 else -1

        
                    
                    