# Given an integer n, print m increasing numbers such that the sum of m
# numbers is equal to n and the GCD of
#  m numbers is maximum among all series possible. If no series is
# possible then print “-1”.


# Input  : n = 24,
#          m = 3  
# Output : 4 8 12

def largestSeries(n, m):
  b = int(n/(m*(m+1)/2))
  
  if b == 0:
    return - 1
    
  pass 


  