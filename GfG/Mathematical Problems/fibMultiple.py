# Check if nTh fibonacci is divisible by 10.

def fib(n):
  a = 0
  b = 1
  if n <= 1:
    return n
    
  for i in range(2, n + 1):
    a, b = b, a + b
    
  return b
  
def isMultipleof10(n):
  x = fib(n)
  return (x % 10 == 0)
  