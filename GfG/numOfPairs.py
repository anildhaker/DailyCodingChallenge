# Count number of pairs (A <= N, B <= N) such that gcd (A , B) is B
# Givenanumbern.Weneedfindthenumberoforderedpairsofa and bsuchgcd(a, b)
# is b itself

# Algo - a will be the multiple of b, such that a <=n
# for a number i -- number of multiples will be less than floor(n/i)
# so we need to sum floor(n/i) for i = 1 to n.
import math

def numPairs(n):
  total = 0 
  for i in range(1, n + 1):
    total += math.floor(n / i)
    
  return total 

print(numPairs(3))