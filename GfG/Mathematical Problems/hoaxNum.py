# hoax num - sum of digits of prime factors = sum of digits of num.
# num must be composite num
# 1 is not included in sum of prime factors.

def num_dig_sum(x):
  total = 0
  while x > 0:
    total += x % 10
    x = x // 10
  return total

# print(num_dig_sum(229))
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

def isHoax(n):
  primes = []
  is_prime = SieveOfEratosthenes(n)

  factors = []
  for i in range(1, n + 1):
    if n % i == 0:
      factors.append(i)
  if len(factors) == 2:
    return False
    
  for i in factors:
    if is_prime[i] == True:
      primes.append(i)

  primes_sum = 0
  for i in primes:
    x = num_dig_sum(i)
    primes_sum += x
    
  if primes_sum == num_dig_sum(n):
    return True
  return False
  
print(isHoax(22))
print(isHoax(84))
print(isHoax(19))
