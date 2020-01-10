# modular exponentiation
# (ab) mod p = ( (a mod p) (b mod p) ) mod p

def modExpo(x, y, p):
  res = 1
  x = x % p
  
  while (y > 0):
    if y & 1 == 1:
      res = (res * x) % p
      print("inside if ",y)
    
    print('y before ',y)
    y = y >> 1
    print('y after ', y)
    print("x before ",x)
    x = (x * x) % p
    print("x after ",x)

    
  return res

print(modExpo(3,200,50))