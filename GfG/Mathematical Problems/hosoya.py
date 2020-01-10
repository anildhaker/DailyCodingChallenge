# print hosaya triangle

def hosoya(n, m):
  if ((n == 0 and m == 0) or
      (n == 1 and m == 0) or
      (n == 1 and m == 1) or
      (n == 2 and m == 1)):
      return 1

  if n > m:
    return hosoya(n - 1, m) + hosoya(n - 2, m)
    
  elif m == n:
    return hosoya(n - 1, m - 1) + hosoya(n - 2, m - 2)
    
  else:
    return 0
    
def printHosoya(n):
  for i in range(n):
    for j in range(i + 1):
      print(hosoya(i, j), end=" ")
    print()

printHosoya(5)

      
  