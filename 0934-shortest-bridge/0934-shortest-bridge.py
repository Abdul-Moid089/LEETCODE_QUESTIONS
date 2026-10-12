from collections import deque

class Solution:
    def shortestBridge(self, grid: list[list[int]]) -> int:
        n = len(grid)
        visited = set()
        queue = deque()
        
        def dfs(r, c):
            if r < 0 or c < 0 or r >= n or c >= n or grid[r][c] == 0 or (r, c) in visited:
                return
            visited.add((r, c))
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n:
                    if grid[nr][nc] == 0 and (nr, nc) not in visited:
                        queue.append((nr, nc, 0))
                        visited.add((nr, nc))
                    elif grid[nr][nc] == 1:
                        dfs(nr, nc)

        found = False
        for i in range(n):
            if found:
                break
            for j in range(n):
                if grid[i][j] == 1:
                    dfs(i, j)
                    found = True
                    break

        while queue:
            r, c, dist = queue.popleft()
            
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in visited:
                    if grid[nr][nc] == 1:
                        return dist + 1
                    visited.add((nr, nc))
                    queue.append((nr, nc, dist + 1))
        
        return 0