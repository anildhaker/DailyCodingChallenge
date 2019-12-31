# find number of digits in nth fib number
# finding fib(n) then counting digits will cause overflow.
# so we will use Binet's formula.
# fib(n) = (Φn - Ψ-n) / √5
# where
# Φ = (1 + √5) / 2
# Ψ = (1 - √5) / 2

# Approximate it for large n -- fib(n) = round(Φn / sqrt(5)) 
import math
def numOfDigits(n):
  if n == 1:
    return 1
    
  fib_n = round(pow((1 + math.sqrt(5)) / 2, n)/math.sqrt(5))
  return math.ceil(math.log10(fib_n))

print(numOfDigits(10))

