def plusMinus(arr):
  for i in range(len(arr)):
    if arr[i] > 0:
      arr[i] = 1
    elif arr[i] < 0:
      arr[i] = -1
  
  print('{:.6f}\n{:.6f}\n{:.6f}'.format(arr.count(1)/len(arr), arr.count(-1)/len(arr), arr.count(0)/len(arr)))