# divide the 1 to n in two sets, also diff of sum of sets = m, gcd(sum_set1,sum_set2) = 1

def gcd(a, b):
  if a == 0:
    return b
  return gcd(b % a, a)
  
def isSplittable(n,m):
  total = int(n*(n + 1)/ 2)
  
  sum1 = int((total + m) / 2)
  
  sum2 = total - sum1

  if total < m:
    return False

  if sum1 + sum2 == total and abs(sum1 - sum2) == m:
    return (gcd(sum1, sum2) == 1)
  return False
  
x = isSplittable(5,7)
print(x)