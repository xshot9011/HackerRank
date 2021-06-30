def countingValleys(steps, path):
  high_level = 0
  valley_count = 0

  for i in path:
    if i == 'D':
      high_level -= 1
    else:
      high_level += 1
    if high_level == 0 and i == 'U':
      valley_count += 1

  return valley_count