def jumpingOnClouds(c):
  index = 0
  shortest_step = 0

  while index < len(c)-1:
    if index+2 < len(c):
      if c[index+2] == 0:
        index += 1
    index += 1
    shortest_step += 1
    
  return shortest_step