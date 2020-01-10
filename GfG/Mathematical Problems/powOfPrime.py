# Finding power of prime number p in n!

# eg. n = 4 p =2 --> 4! = 24 = 2*2*2*3 --> should return 4 else return Zero.

# Just count power of p from 1 to n. and add them.

def powerPinNfactorial(n, p):
  ans = 0
  temp = p
  while (temp <= n):
    print("n-->",n)
    ans += n / temp
    print("ans-->",ans)
    temp = temp * p
    print("temp-->",temp)
      
  return ans
  

print(powerPinNfactorial(8, 2))





  
  


