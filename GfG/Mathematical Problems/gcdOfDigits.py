# finding gcd of digits of a number

def gcd(a, b):
  if a == 0:
    return b
  return gcd(b % a, a)
  

def gcd_digits(num):
  g_c_d = 0 
  while num > 0:
    curr = num % 10
    g_c_d = gcd(curr, g_c_d)
    num = num // 10
    
  return g_c_d
    
    
  
print(gcd_digits(123))