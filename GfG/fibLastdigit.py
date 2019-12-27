# Fib number unit's place digit repeates after every 60 numbers.

arr = [0 for i in range(100)]
arr[0] = 0
arr[1] = 1

for i in range(2, 99):
  arr[i] = arr[i - 1] + arr[i - 2]

for i in range(1, 99):
  if (arr[i] % 10 == 0) and (arr[i + 1] % 10 == 1):
    break
print("Index after sequence repeats -->", i)
  


    
  

  