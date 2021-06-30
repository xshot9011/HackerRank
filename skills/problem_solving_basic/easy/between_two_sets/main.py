def get_gcd(x, y):
  while(y):
    x, y = y, x % y
  
  return x

def get_lcm(x, y):
  return int(abs(x*y)/get_gcd(x,y))


def getTotalX(a, b):
  lcm = get_lcm(a[0], a[1]) if len(a) >= 2 else a[0]
  gcd = get_gcd(b[0], b[1]) if len(b) >= 2 else b[0]
  count = 0

  for i in range(2, len(a)):
    lcm = get_lcm(lcm, a[i])
  for i in range(2, len(b)):
    gcd = get_gcd(gcd, b[i])
  for i in range(lcm, gcd+1, lcm):
    print(i)
    if gcd%i==0:
      count += 1

  return count
