def birthday(s, d, m):
  tp = (len(s)-m) + 1
  return len([1 for i in range(tp) if sum(s[i:i+m])==d])
