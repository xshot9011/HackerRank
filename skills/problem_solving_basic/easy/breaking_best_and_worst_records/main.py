def breakingRecords(scores):
  n = len(scores)
  max_num = scores[0]
  max_count = 0
  min_num = scores[0]
  min_count = 0
  
  for i in range(len(scores)):
    if scores[i] > max_num:
      max_count += 1
      max_num = scores[i]
    elif scores[i] < min_num:
      min_count += 1
      min_num = scores[i]
  
  return max_count, min_count