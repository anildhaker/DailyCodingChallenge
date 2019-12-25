# finding largest prime factor

import math as m
def maxPrime(n):
  Max = -1
  
  while n % 2 == 0:
    Max = 2
    n = int(n // 2)
    
  for i in range(3, int(m.sqrt(n)) + 1):
    while n % i == 0:
      Max = i
      n = int(n // i)
      
  if n > 2:
    Max = n
    
  return Max

