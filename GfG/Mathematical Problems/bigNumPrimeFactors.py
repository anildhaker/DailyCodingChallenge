# find all the prime factors and their powers for a big number.
# Will not use SOE because for big numbers it is not space optimized. 

import math 
def primeFactors(n):
  count = 0
  
  # dealing with 2
  
  while n % 2 == 0:
    count += 1
    n = int(n // 2)
    
  if count > 0:
    print(2, count)

  for i in range(3, int(math.sqrt(n)) + 1, 2):
    count = 0
    while (n % i == 0):
      count += 1
      n = int(n / i)
      
    if count > 0:
      print(i, count)

    
  if n > 2:
    print(n, 1)
    
n = 1000000000000000000
primeFactors(n)
      
    