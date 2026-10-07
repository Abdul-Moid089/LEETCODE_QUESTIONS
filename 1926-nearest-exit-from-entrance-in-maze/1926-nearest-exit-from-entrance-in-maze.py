from collections import deque

class Solution:
    def nearestExit(self, maze: list[list[str]], entrance: list[int]) -> int:
        rows, cols = len(maze), len(maze[0])
        start_r, start_c = entrance
        
        queue = deque([(start_r, start_c, 0)])
        maze[start_r][start_c] = '+'
        
        while queue:
            r, c, steps = queue.popleft()
            
            for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] == '.':
                    if nr == 0 or nr == rows - 1 or nc == 0 or nc == cols - 1:
                        return steps + 1
                    
                    maze[nr][nc] = '+'
                    queue.append((nr, nc, steps + 1))
                    
        return -1