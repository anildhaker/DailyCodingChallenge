# find sum in O(log(n)) or linear time
# S(n) = F(n+2) – 1

def fib(n):
  a = 0
  b = 1
  
  if n == 0:
    return a
    
  elif n == 1:
    return b

  else:
    for i in range(2, n + 1):
      a, b = b, a + b
    return b
    
  
def fibSum(n):
  return fib(n + 2) - 1
  
print(fibSum(4))
    


