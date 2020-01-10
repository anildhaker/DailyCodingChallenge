# Nth fib number using Golden ratio.
# nth fib = (n-1)th fib * golden ratio
# round up each stage to get the correct result.

Phi = 1.6180339

f = [0, 1, 1, 2, 3, 5]

def fib(n):
  if n < 6:
    return f[n]

  t = 5
  tn = 5
  
  while t < n:
    tn = round(tn * Phi)
    print(t)
    t += 1
  return tn
  
n = 9
print(n, "th Fibonacci Number =", fib(n)) 