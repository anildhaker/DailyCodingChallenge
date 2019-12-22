# kth Prime factor of a given number
import math
def SOE(n):
  prime = [True for i in range(n + 1)]
  p = 2
  while (p * p <= n):
    if prime[p] == True:
      for i in range(2*p,n+1,p):
        prime[i] = False
    p += 1

  prime[0] = False
  prime[1] = False

  return prime

def allPrimeFactors(n):
  p_factors = []
  while n % 2 == 0:
    p_factors.append(2)
    n = int(n // 2)

  for i in range(3, (int(math.sqrt(n)) + 1), 2):
    while n % i == 0:
      p_factors.append(i)
      n = int(n // i)
      
  if n > 2:
    p_factors.append(n)

  return p_factors
    
    
def kthPrime(n,k):
  x = allPrimeFactors(n)
  print(x)
  if len(x) <= k:
    return False
  return x[k-1]


print(kthPrime(225, 2))
print(kthPrime(81, 5))
# Input : n = 225, k = 2        
# Output : 3
# Prime factors are 3 3 5 5. Second
# prime factor is 3.

# Input : n = 81, k = 5
# Output : -1
# Prime factors are 3 3 3 3

  

