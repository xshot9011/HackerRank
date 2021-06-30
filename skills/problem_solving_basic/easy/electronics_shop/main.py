def getMoneySpent(keyboards, drives, b):
  max_price = -1
  keyboards_prices = sorted(keyboards, reverse=True)
  drive_prices = sorted(drives)
  
  for keyboard_price in keyboards_prices:
    for drive_price in drive_prices:
      if keyboard_price + drive_price > b:
        break
      max_price = max(max_price, keyboard_price + drive_price)
  
  return max_price