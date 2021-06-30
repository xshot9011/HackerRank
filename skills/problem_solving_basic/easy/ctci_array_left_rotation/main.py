def rotLeft(a, d):
  new_start_index = (0+d)%len(a)
  return a[new_start_index:]+a[:new_start_index]
