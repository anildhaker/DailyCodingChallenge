# find sum of all divisors of numbers from 1 to n.

# naive Approach

def SumAllDivisors(n):
  sum = 0
  
  for i in range(1, n + 1):
    j = 1
    while (j % j <= i):
      if i % j == 0:
        if i / j == j:
          sum += j
          
        else:
          sum += j + i / j
          
      j += 1
  return sum


# time complexity = O(n*sqrt(n))


# Method 2 -
# there is repeating pattern

# Let n = 6,
# => F(1) + F(2) + F(3) + F(4) + F(5) + F(6)
# => 1 will occurs 6 times in F(1), F(2),
#    F(3), F(4), F(5) and F(6)
# => 2 will occurs 3 times in F(2), F(4) and
#    F(6)
# => 3 will occur 2 times in F(3) and F(6)
# => 4 will occur 1 times in F(4)
# => 5 will occur 1 times in F(5)
# => 6 will occur 1 times in F(6)
import math
def EffSumAllDivisors(n):
  for i in range(1, n + 1):
    sum = sum + i*math.floor(n / i)
    
  return int(sum)


      