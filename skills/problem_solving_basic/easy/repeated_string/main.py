def repeatedString(s, n):
  COUNT_CHAR = 'a'
  number_a = 0
  
  number_a += (n // len(s)) * s.count(COUNT_CHAR)
  number_a += s[:(n % len(s))].count(COUNT_CHAR)
    
  return number_a