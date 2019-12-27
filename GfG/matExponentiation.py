# find nth Fibonacci number in O(log(n)) time.
# we use matrix exponentiation to achieve this.

def mul(a, b):  #multiplying 2 matrices
  mul = [[0 for i in range(3)] for j in range(3)]

  for i in range(3):
    for j in range(3):
      mul[i][j] = 0 
      for k in range(3):
        mul[i][j] += a[i][k] * b[k][j]
        
  # update and store result in matrix a
  
  for i in range(3):
    for j in range(3):
      a[i][j] = mul[i][j]

  return a
  
# M = [[1, 1, 1], [1, 0, 0], [0, 1, 0]]
# print(mul(M,M))

def power(F, n):
  M = [[1, 1, 1], [1, 0, 0], [0, 1, 0]]

  if n == 1:
    return F[0][0] + F[0][1]
  
  power(F, int(n / 2))

  F = mul(F, F)
  
  if (n % 2 != 0):
    F = mul(F, M)

  return F[0][0] + F[0][1]


def findNthTerm(n):
  F = [[1, 1, 1], [1, 0, 0], [0, 1, 0]]
  return power(F, n - 2)


print(findNthTerm(5))