class Solution:
    def dfs(self, grid, r, c):
        rows = len(grid)
        cols = len(grid[0])

        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != 0:
            return

        grid[r][c] = 1

        self.dfs(grid, r + 1, c)
        self.dfs(grid, r - 1, c)
        self.dfs(grid, r, c + 1)
        self.dfs(grid, r, c - 1)

    def closedIsland(self, grid):
        rows = len(grid)
        cols = len(grid[0])

        for r in range(rows):
            self.dfs(grid, r, 0)
            self.dfs(grid, r, cols - 1)

        for c in range(cols):
            self.dfs(grid, 0, c)
            self.dfs(grid, rows - 1, c)

        count = 0

        for r in range(1, rows - 1):
            for c in range(1, cols - 1):
                if grid[r][c] == 0:
                    count += 1
                    self.dfs(grid, r, c)

        return count