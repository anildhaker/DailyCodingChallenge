#find sqrt under modulo.
#n - given number, p - of form 4*i + 3

# iterate from 2 to p-1 and check 
def sqrtModulo(n, p):
  n = n % p
  
  for x in range(2, p - 1):
    if (x * x) % p == n:
      print(x, ' is the root')
      return
      
  print("root does not exist")
  return - 1
  
sqrtModulo(2,7)
  