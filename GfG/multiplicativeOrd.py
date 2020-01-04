# multiplicative order - under Modulo
# gcd(A,N) = 1 .. find lowest k such that A^k mod(N) = 1
def gcd(a, b):
  if a == 0:
    return b
  return gcd(b % a, a)
  
def multiplicativeOrder(a, n):
  if gcd(a, n) != 1:
    return - 1

  res = 1
  k = 0
  for i in range(1, n):
    res = (res * a) % n
    
    if res == 1:
      k = i
      break
    
  return k
  
print(multiplicativeOrder(4, 7))

# time complexity O(n)

      
   