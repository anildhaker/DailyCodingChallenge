# find the index of fib num in constant time.

def Index_fib(n):
  if n <= 1:
    return n

  res = 1
  a = 0
  b = 1
  
  while b < n:
    res = res + 1
    a, b = b, a + b
    
  return res
  
print(Index_fib(21))