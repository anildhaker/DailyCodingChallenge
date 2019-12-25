# Given a number n, the task is to find the even factor sum of a number.
import math as m 
def sum_even_factors(n):
  # if number is odd then no even factors
  if n % 2 == 1:
    return False
  res = 1 
  for i in range(2, int(m.sqrt(n)) + 1):
    count = 0
    curr_sum = 1   
    curr_term = 1  
    while (n % i == 0):
      count += 1
      print("i-->", i)
      print("n -->",n)
      n = int(n // i)
      print("n -->",n)
      
      if (i == 2 and count == 1):
        curr_sum = 0
        
      curr_term = curr_term * i
      print("curr_term--->",curr_term)
      curr_sum = curr_sum + curr_term
      print("curr_sum -->",curr_sum)

    res = res * curr_sum
    
  if n >= 2:
    res = res * (n + 1)  # case to tackle prime numbers
      
  return res
    

print(sum_even_factors(18))

