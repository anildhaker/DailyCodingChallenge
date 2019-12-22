# a number which has exactly 3 prime factors is -- Sphenic number.
# 30 = 2*3*5 is sphenic but// 60 = 2*2*3*5 is not sphenic number

def SieveOfEratosthenes(n):
  prime = [True for i in range(n + 1)]
  p = 2
  while (p * p <= n):
    if prime[p] == True:
      for i in range(2 * p, n + 1, p):
        prime[i] = False
    p += 1
    
  prime[0] = False
  prime[1] = False
  
  return prime

def isSphenic(n):
  factors = []
  for i in range(1, n + 1):
    if n % i == 0:
      factors.append(i)

  is_prime = SieveOfEratosthenes(n)
  
  count = 0
  for i in factors:
    if is_prime[i] == True:
      count = count + 1
    
  if (count == 3 and len(factors) == 8):
    return True
  return False
  
print(isSphenic(30))
print(isSphenic(60))