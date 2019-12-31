# Sum of even fib numbers .. limit is given.

def sumEvenFib(limit):
  even = []
  a = 0
  b = 1
  
  while (b < limit):
    if b % 2 == 0:
      even.append(b)
    a, b = b, a + b
  print(even)
  return sum(even)


print(sumEvenFib(400))