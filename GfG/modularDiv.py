# modular division

# The task is basically to find a number c such that (b * c) % m = a % m.
# for this to exist inverse of b mod m must exist.
import math
def modInverse(b, m):
  g = math.gcd(b, m)
  
  if g != 1:
    # print("Inverse does not exist")
    return - 1
  
  else:
    return pow(b, m - 2, m)


def modDivide(a, b, m):
  a = a % m
  inverse = modInverse(b, m)
  if inverse == -1:
    print("Division not defined")

  else:
    print("result of division is ->", (inverse * a) % m)

modDivide(8, 3, 5)


    
  