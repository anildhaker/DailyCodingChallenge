# find fib numbers in an array.

import math
def isSquare(n):
  s = int(math.sqrt(n))
  return s * s == n

def fibNumInArray(arr):
  res = []
  for i in arr:
    if (isSquare(5 * i * i + 4) or isSquare(5 * i * i - 4)):
      res.append(i)

  return res
  
array = [4, 2, 8, 5, 20, 1, 40, 13, 23]
print(fibNumInArray(array))