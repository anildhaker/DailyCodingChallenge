# sum of all proper divisors of a number.
# A proper divisor of a natural number is the divisor that is
# strictly less than the number.

def propDivSum(n):
  temp = n 
  sum = 0
  i = 1
  while (i < n):
    if n % i == 0:
      print(i)
      sum += i
    i = i + 1
      
  if n > 2 and n != temp:
    sum += n

  return sum
  
# print(propDivSum(10))
print(propDivSum(36))


# to make it more effiecint .. i < sqrt(n) and if i is proper divisor so will be n/i 

