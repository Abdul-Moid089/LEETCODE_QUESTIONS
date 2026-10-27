class Solution:

  def createGrid(self, m: int, n: int) -> list[str]:
    # Initialize the grid with all obstacles '#'
    grid = [["#" for _ in range(n)] for _ in range(m)]

    # Make the top row free cells '.'
    for j in range(n):
      grid[0][j] = "."

    # Make the last column free cells '.'
    for i in range(m):
      grid[i][n - 1] = "."

    # Convert rows of characters into strings
    return ["".join(row) for row in grid]