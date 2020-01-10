# fib modulo p.
# find the fib term when for the first time fibModp becomes zero.
# concept here is that ..instead of calculating each term and then remainder
# we will just add the remainder of two previous terms. 

def findMinZero(p):
  first = 1
  second = 1
  number = 2
  next = 1
  
  while (next):
    next = (first + second) % p
    first, second = second, next
    number = number + 1
    
  return number
  

print(findMinZero(7))