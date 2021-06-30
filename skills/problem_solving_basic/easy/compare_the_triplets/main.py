def compareTriplets(a, b):
  score1 = 0
  score2 = 0

  for i in range(len(a)):
    if a[i] > b[i]:
      score1 += 1
    elif a[i] < b[i]:
      score2 += 1
  return [score1, score2]
