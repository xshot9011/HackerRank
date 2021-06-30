def pageCount(n, p):
  return min(get_page(0, p-1 if p%2 != 0 else p), \
    get_page(n-1 if n%2 != 0 else n, p-1 if p%2 != 0 else p))

def get_page(start, stop):
  return int(abs(start-stop)/2)
