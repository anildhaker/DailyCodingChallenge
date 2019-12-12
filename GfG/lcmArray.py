#find the lcm of the array

def gcd(a, b):
  if a == 0:
    return b
  return gcd(b%a,a)

def lcm(a,b):
  # a*b = lcm * gcd 
  x = (a * b) / gcd(a, b)
  return x

def arrayLcm(A):
  ans = A[0]
  for i in range(1,len(A)):
    ans = lcm(ans,A[i])
  return ans


A = [1, 2, 8, 3]
print(arrayLcm(A))

  