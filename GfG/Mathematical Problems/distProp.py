# Given three integers x, y, z, the task is to compute the value of GCD(LCM(x,y), LCM(x,z)).
# Where, GCD = Greatest Common Divisor, LCM = Least Common Multiple

# We will use distributive prop - GCD(LCM(x,y), LCM(x,z)) = LCM(x,GCD(y,z))

def gcd(a, b):
  if a == 0:
    return b
  return gcd(b % a, a)
  
def distValue(x, y, z):
  p = gcd(y, z)
  v = x * p / gcd(x, p)
  return v
  
print(distValue(15,20,100))