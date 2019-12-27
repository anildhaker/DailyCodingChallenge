# represent any positive interger as sum of two non-consecutive fib numbers.

def nearestSmallEqFib(n):
  if n == 0 or n == 1:
    return n
    
  a = 0
  b = 1
  
  while b <= n:
    a, b = b, a + b
    
  return a
  
def fibRepresentation(n):
  while n > 0:
    f = nearestSmallEqFib(n)
    print(f)
    n = n - f
    
fibRepresentation(30)
# print(nearestSmallEqFib(30))

