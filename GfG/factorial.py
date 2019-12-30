# Recursive solution

def factorial(n):
  if n == 0 or n == 1:
    return 1
    
  else:
    return n * factorial(n - 1)
    

print(factorial(5))

# iterative solution
def fact_iterative(n):
  res = 1
  i = 1
  while i <= n:
    res = res * i
    i = i + 1
    
  return res
  
print(fact_iterative(5))


