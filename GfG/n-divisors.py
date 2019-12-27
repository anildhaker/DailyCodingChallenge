# find number with n divisors in a given range.
# Given three integers a, b, n .Your task is to print number of numbers between a and b including them also which have n-divisors. A number is called n-divisor if it has total n divisors including 1 and itself.
# Examples:

# Input  : a = 1, b = 7, n = 2
# Output : 4
# There are four numbers with 2 divisors in 
# range [1, 7]. The numbers are 2, 3, 5, and 7.
import math 
def SOE(x):
  prime = [True] * (x + 1)
  
  prime[0] = False
  prime[1] = False

  p = 2
  while (p * p <= x):
    if prime[p] == True:
      for i in range(2 * p, x + 1, p):
        prime[i] = False

    p += 1

def numDivisors(n):
  total = 0
  for i in range(1, int(math.sqrt(n)) + 1):
    if n % i == 0:
      total += 1
      n = int(n // i)

  if n > 2:
    total = total + 1

  return total  

def nDivisors(a, b, n):
  result = 0
  for i in range(a, b + 1):
    if numDivisors(i) == n:
      result += 1
      
  return result

print(nDivisors(1,7,2))