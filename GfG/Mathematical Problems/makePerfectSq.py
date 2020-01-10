# Find minimum number to be divided to make a number a perfect square.
#  ex - 50 dividing it by 2 will make it perfect sq. So output will be 2.

# A number is the perfect square if it's prime factors have the even power.

# all the prime factors which has the odd power should be multiplied and returned(take 1 element at once).

import math

def findMinNum(n):
  # 2 is only even number so counting the power of 2
  count = 0
  ans = 1 
  while n % 2 == 0:
    count += 1
    n = int(n // 2)
    
  # if count is not even then we must remove one 2.
  if count % 2 != 0:
    ans = ans * 2
    

  for i in range(3, int(math.sqrt(n)) + 1, 2):
    count = 0
    while n % i == 0:
      count += 1
      n = int(n // i)
      
    if count % 2 != 0:
      ans = ans*i 


  if n > 2:
    ans = ans * n
    

  return ans
  
print(findMinNum(72))