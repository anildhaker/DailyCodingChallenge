# Given a non-negative integer n. The problem is to find the sum of the largest
# prime factor of each number less than equal to n.

def sumOfLargestPrimeFactors(n):
  # we will use SOE
  
  prime = [0] * (n + 1)  # initializing all numbers with zero.
  
  sum = 0
  prime[0] = 0
  prime[1] = 0

  p = 2
  while (2* p <= n):
    if prime[p] == 0:
      for i in range(2 * p, n + 1, p):
        prime[i] = p
    p += 1


  for p in range(2, n + 1):
    # if p is non- prime then prime[p] will give highest prime factor.
    if prime[p]:
      sum = sum + prime[p]

    else:
      sum = sum + p  # case when p is prime.
      
  return sum

print(sumOfLargestPrimeFactors(12))


  
    
