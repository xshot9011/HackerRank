def catAndMouse(x, y, z):
  distance = {
    abs(x-z): 'A',
    abs(y-z): 'B'
  }
  
  if len(distance) == 1:
    return 'Mouse C'
  
  return 'Cat {}'.format(distance[min(distance)])