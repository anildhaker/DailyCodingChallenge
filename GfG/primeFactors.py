# for 12 -- print 2,2,3
import math 
def primeFactors(n):

  while n % 2 == 0 and n > 0:
    print(2)
    n = n // 2
    
  # n becomes odd after above step.
  for i in range(3, int(math.sqrt(n) + 1), 2):
    
    while n % i == 0:
      print(i)
      n = n // i
      
  # until this stage all the composite numbers have been taken care of.
      
  if n > 2:
    print(n) 
  
    
primeFactors(315)