pre_matrix = [
  [[8, 1, 6], [3, 5, 7], [4, 9, 2]],
  [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
  [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
  [[2, 9, 4], [7, 5, 3], [6, 1, 8]], 
  [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
  [[4, 3, 8], [9, 5, 1], [2, 7, 6]], 
  [[6, 7, 2], [1, 5, 9], [8, 3, 4]], 
  [[2, 7, 6], [9, 5, 1], [4, 3, 8]],
]

def formingMagicSquare(s):
  global pre_matrix
  cost = []
  
  for matrix in pre_matrix:
    total_cost = 0
    for matrix_row, s_row in zip(matrix, s):
      for x_i, s_i in zip (matrix_row, s_row):
        if not x_i == s_i:
          total_cost += abs(x_i-s_i)
    cost.append(total_cost)

  return min(cost)