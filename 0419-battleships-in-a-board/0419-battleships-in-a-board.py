class Solution:

  def countBattleships(self, board: list[list[str]]) -> int:
    m, n = len(board), len(board[0])
    count = 0

    for i in range(m):
      for j in range(n):
        if board[i][j] == 'X':
          # Check if there is an 'X' directly above
          if i > 0 and board[i - 1][j] == 'X':
            continue
          # Check if there is an 'X' directly to the left
          if j > 0 and board[i][j - 1] == 'X':
            continue
          # If neither exists, this is the top-left cell of a new battleship
          count += 1

    return count