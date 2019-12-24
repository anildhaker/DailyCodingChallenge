# find sum of all factors.

# method 1 - simple iterative solution
import math
def sumFactors(n):
  res = 0
  
  for i in range(2, int(math.sqrt(n)) + 1):
    if n % i == 0:
      if (i == int(n / i)):
        res = res + i
      else:
        res = res + i + int(n // i)

  return (res + n + 1)
  

print(sumFactors(30))


# Mehtod 2 - efficient approach.
# Sum of divisors = (1 + p1 + p12 ... p1a1) * 
#                   (1 + p2 + p22 ... p2a2) *
#                   .............................................
#                   (1 + pk + pk2 ... pkak)

def allPrimeFactors(n):
  prime = []
  while n % 2 == 0:
    prime.append(2)
    n = int(n // 2)
    
  for i in range(3, int(math.sqrt(n) + 1), 2):
    while n % i == 0:
      prime.append(i)
      n = int(n // i)
  
  if n > 2:
    prime.append(n)

  return prime


def effFactorSum(n):
  x = allPrimeFactors(n)
  d = {}
  for i in x:
    if i not in d.keys():
        d[i] = 1
    else:
        d[i] += 1
  
  net_sum = 1
  for i in d:
    s = 0 
    for j in range(0, d[i] + 1):
       s += i**j
    net_sum = net_sum*s
    
  return net_sum
  
print(effFactorSum(30))

# time complexity O(n*n)