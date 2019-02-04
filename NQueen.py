# this is N Queen Problem
# learining Back Tracking

# You have an N by N board.
# Write a function that returns the number of possible arrangements of the board
# where N queens can be placed on the board without threatening each other.
# i.e. no two queens share the same row, column, or diagonal.

def n_queens(n, board=[]):
  if n == len(board):
    return 1
  
  count = 0
  for col in range(n):
    board.append(col)
    if is_valid(board):
      count += n_queens(n, board)
    board.pop()
  return count
  
def is_valid(board):
    current_queen_row, current_queen_col = len(board) - 1, board[-1]
    # Check if any queens can attack the last queen.
    for row, col in enumerate(board[:-1]):
        diff = abs(current_queen_col - col)
        if diff == 0 or diff == current_queen_row - row:
            return False
    return True



  