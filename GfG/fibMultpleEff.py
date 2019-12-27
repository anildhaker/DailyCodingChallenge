# Efficient way to check if Nth fibonacci number is multiple of a given number.

# for example multiple of 10.

# num must be multiple of 2 and 5.
# Multiples of 2 in Fibonacci Series :
# 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 ….
# every 3rd number - is divisible by 2.
# Multiples of 5 in Fibonacci Series :
# 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 ……
# Every 5th number is divisible by 5.

# => Every 15th number will be divisible by 10. So we only need to check if n is divisible
# by 15 or not. We do not have to calculate the nth Fib number.

def isDivisibleby_10(n):
  if n % 15 == 0:
    return True
  return False
  