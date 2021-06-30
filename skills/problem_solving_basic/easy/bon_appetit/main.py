def bonAppetit(bill, k, b):
  fair_charged_price = int(sum(bill)/2)
  anna_charged_price = int((sum(bill)-bill[k])/2)

  if b == anna_charged_price:
    print('Bon Appetit')
  else:
    print(b-anna_charged_price)