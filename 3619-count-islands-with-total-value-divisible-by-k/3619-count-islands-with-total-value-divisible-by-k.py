class Solution:
    def countIslands(self, grid, k):
        m = len(grid)
        n = len(grid[0])

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        ans = 0

        for i in range(m):
            for j in range(n):

                if grid[i][j] == 0:
                    continue

                # Start a new island
                total = grid[i][j]
                grid[i][j] = 0

                stack = [(i, j)]

                while stack:
                    x, y = stack.pop()

                    for dx, dy in directions:
                        nx = x + dx
                        ny = y + dy

                        if (0 <= nx < m and
                            0 <= ny < n and
                            grid[nx][ny] > 0):

                            total += grid[nx][ny]

                            # Mark visited
                            grid[nx][ny] = 0

                            stack.append((nx, ny))

                # Check island's total value
                if total % k == 0:
                    ans += 1

        return ans