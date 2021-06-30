def migratoryBirds(arr):
  arr_uni = sorted(set(arr))
  counting = {}
  
  for i in arr_uni:
    counting[i] = arr.count(i)

  return max(counting, key=counting.get)