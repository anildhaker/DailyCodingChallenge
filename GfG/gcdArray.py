def gcd(a, b):
  if a == 0:
    return b
  return gcd(b % a, a)
  
def gcdArray(A):
  ans = A[0]
  for i in range(1, len(A)):
    ans = gcd(ans, A[i])
    
  return ans

A = [1, 2, 3]
print(gcdArray(A))