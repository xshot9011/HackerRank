def minimumBribes(q):
  first_pointer = 1
  second_pointer = 2
  third_pointer = 3
  bribe_number = 0
  
  for index in range(len(q)):
    if q[index] == first_pointer:
      first_pointer = second_pointer
      second_pointer = third_pointer
      third_pointer += 1
    elif q[index] == second_pointer:
      second_pointer = third_pointer
      third_pointer += 1
      bribe_number += 1
    elif q[index] == third_pointer:
      third_pointer += 1
      bribe_number += 2
    else:
      print('Too chaotic')
      return
  print(bribe_number)
