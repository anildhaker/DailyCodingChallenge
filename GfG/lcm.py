# lcm of two numbers 

def gcd(a, b):
  if a == 0:
    return b
  return gcd(b%a,a)

def lcm(a,b):
  # a*b = lcm * gcd 
  x = a * b / gcd(a, b)
  return x
  

  