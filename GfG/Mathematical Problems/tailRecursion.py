# tail recursion for fib numbers

def tailRecFib(n, a=0, b=1):
  if n == 0:
    return a
  if n == 1:
    return b
  return tailRecFib(n - 1, b, a + b)
  
print(tailRecFib(9))