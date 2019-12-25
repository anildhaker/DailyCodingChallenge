# objective is to find minimum sum of factors of a number.

# 12 - 12*1 sum = 13,  12 - 2*6 sum = 8

# idea here is start from factor 2 and because all the lowest possible combination of
# factors will give the desired minimum sum. 

def minSumFactors(n):
  sum = 0
  i = 2
  while (i * i <= n):
    while (n % i == 0):
      sum = sum + i
      n = int(n//i)
      
    i = i + 1
    
  if sum != 0:
    return sum + n
  else:
    return (n + 1)
    
# driver code
print(minSumFactors(12))
print(minSumFactors(11))

    
  
  