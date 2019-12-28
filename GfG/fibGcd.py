# gcd of Fib(m) and fib(n)  -- is same as fib(gcd(m,n))

def gcd(a, b):
  if a == 0:
    return b
  return gcd(b % a, a)
  

Max = 1000

# cosidering only first 1000 fib numbers.
# f = [0 for i in range(Max)]
def fib(n):
  f = [0 for i in range(n+1)]
  
  f[0] = 0
  f[1] = 1
  f[2] = 1
  if n <= 2:
    return f[n]
  else:
    if f[n - 1] == 0:
      f[n - 1] = fib(n - 1)
    
    if f[n - 2] == 0:
      f[n - 2] = fib(n - 2)
      
  f[n] = f[n - 1] + f[n - 2]
  return f[n]


def gcdFibM_N(m, n):
  return fib(gcd(m, n))
  
print(gcdFibM_N(3, 12))
# print(gcd(3, 12))
# print(fib(9))