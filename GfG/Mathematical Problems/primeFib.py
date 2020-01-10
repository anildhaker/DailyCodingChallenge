# find numbers which are both Fib and prime for a given limit.

# A number is Fibonacci if and only if one or both of (5*n2 + 4)
# or (5*n2 – 4) is a perfect square

import math
def isSquare(n):
  s = int(math.sqrt(n))
  return s * s == n

def primeAndFib(n):
  prime = [True for i in range(n + 1)]
  
  prime[0] = False
  prime[1] = False

  p = 2
  while (p * p <= n):
    if prime[p] == True:
      for i in range(2 * p, n + 1, p):
        prime[i] = False

    p = p + 1

  for i in range(2, n + 1):
    if (prime[i] and (isSquare(5 * i * i + 4) > 0 or isSquare(5 * i * i - 4) > 0)):
      print(i, end=" ")
  print()   
  
primeAndFib(30)

    

    
  
        
    