def kangaroo(x1, v1, x2, v2):
  while True:
    if x1 == x2:
      return 'YES'
    elif (v1>=v2 and x1>x2) or (v2>=v1 and x2>x1):
      return 'NO'
    else:
      x1 += v1
      x2 += v2
