from typing import List

class NumArray:
  def __init__(self, matrix: List[List[int]]) -> None:
    ROWS, COLS = len(matrix), len(matrix[0])
    self.prefix = [[0] * (COLS + 1) for _ in range(ROWS + 1)]
    
    for row in range(ROWS):
      row_prefix = 0
      for col in range(COLS):
        row_prefix += matrix[row][col]
        col_prefix = self.prefix[row][col + 1]
        self.prefix[row+1][col+1] = row_prefix + col_prefix
        
  def sum_region(self, row_1: int, col_1: int, row_2: int, col_2: int):
    return self.prefix[row_2+1][col_2+1] - self.prefix[row_2+1][col_1] - self.prefix[row_1][col_2+1] + self.prefix[row_1][col_1]
  
num_array = NumArray([[3,0,1,4,2],
                      [5,6,3,2,1],
                      [1,2,0,1,5],
                      [4,1,0,1,7],
                      [1,0,3,0,5]])
print(num_array.sum_region(2,1,4,3))
