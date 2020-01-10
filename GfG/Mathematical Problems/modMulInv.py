# modular multiplicative inverse.
#  a x ≡ 1 (mod m)
# a and m should be relatively prime for x to exist

# we want to find x in range (0 to m-1)

#naive approach - try all values (1,m)
def mulInverse(a, m):
  a = a % m
  for x in range(1, m):
    if (x * a) % m == 1:
      return x
  return 1
    
print(mulInverse(3, 11))

# time complexity - O(m)


  