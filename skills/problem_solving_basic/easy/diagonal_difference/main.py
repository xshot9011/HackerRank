def diagonalDifference(arr):
  dia1 = 0
  dia2 = 0

  for i in range(len(arr)):
    dia1 += arr[i][i]
    dia2 += arr[len(arr)-1-i][i]

  return abs(dia1-dia2)