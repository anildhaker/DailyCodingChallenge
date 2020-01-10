# print n-th fibonacci number

# Recusion 
def fib(n):
  if n == 0:
    return 0

  if n == 1:
    return 1

  return fib(n - 1) + fib(n - 2)
  

# print(fib(9))

# Time Complexity - T(n) = T(n-1) + T(n-2)

# Dynamic Programming

def fibonacci(n):
  fibArray = [0, 1]
  
  while len(fibArray) < n + 1:
    fibArray.append(0)

  if n <= 1:
    return n
    
  else:
    if fibArray[n - 1] == 0:
      fibArray[n - 1] = fibonacci(n - 1)
      
    if fibArray[n - 2] == 0:
      fibArray[n - 2] = fibonacci(n - 2)
  
  fibArray[n] = fibArray[n - 1] + fibArray[n - 2]
  
  return fibArray[n]

print(fibonacci(9))

  