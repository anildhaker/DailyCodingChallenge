# gcd of floating point numbers

import math

def gcd_float(a, b):
  if a < b :
    return gcd_float(b, a)
    
  if b < 0.001:
    return a

  else:
    return gcd_float(a, (a // b) * b)
    

#what if we try normal appraoch
def gcd(a, b):
  if a == 0:
    return b
  
  return gcd(b % a, a)
  


print(gcd_float(1.20,22.5))