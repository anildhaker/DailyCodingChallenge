# check if a given number is fib number.

# fib num has a property - 5*n2 + 4) or (5*n2 – 4) is perfect square.

import math

def isPerfectSq(x):
  s = int(math.sqrt(x))
  return (s * s == x)
  
def isFibonacci(n):
  return isPerfectSq(5 * n * n + 4) or isPerfectSq(5 * n * n - 4)
  

