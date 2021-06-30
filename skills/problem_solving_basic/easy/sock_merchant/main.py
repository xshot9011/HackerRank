def sockMerchant(n, ar):
  pair_number = 0
  sock_data = {}

  for sock in ar:
    if sock in sock_data:
      pair_number += 1
      del sock_data[sock]
    else:
      sock_data[sock] = None

  return pair_number