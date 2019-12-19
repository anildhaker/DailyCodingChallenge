# gcd of floating point numbers

import math

def gcd(a, b):
  if a < b :
    return gcd(b, a)
    
  if b < 0.001:
    return a

  else:
    return gcd(a, math.floor(a / b) * b)
    