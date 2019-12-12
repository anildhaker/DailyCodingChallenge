# two arrays give - 1 contains terms for numerator and other for denominator

def gcd(a, b):
  if a == 0:
    return b
  return gcd(b%a,a)

def prodFraction(A, B):
  
  num = 1
  deno = 1

  assert (len(A) == len(B))
  
  for i in range(len(A)):
    num = num * A[i]
    deno = deno * B[i]
    
  GCD = gcd(num, deno)
  
  num = num / GCD
  deno = deno / GCD
  
  print(("{}"+ "/" + "{}").format(num,deno))
  
A = [1, 2, 5]
B = [2, 1, 6]
prodFraction(A,B)