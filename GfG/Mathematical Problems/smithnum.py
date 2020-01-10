# Smith Number
# Given a number n, the task is to find out whether this number is smith or not.
# A Smith Number is a composite number whose sum of digits is equal to the
# sum of digits in its prime factorization.

import math

MAX = 10000

primes = []
def sieveSundram():
  marked = [0] * (int(MAX / 2) + 100)
  i = 1

  while i <= ((math.sqrt (MAX)-1)/2) : 
      j = (i* (i+1)) << 1
      while j <= MAX/2 : 
        marked[j] = 1
        j = j+ 2 * i + 1
      i = i + 1

  primes.append(2)
  
  i=1
  while i <= MAX /2 : 
    if marked[i] == 0 : 
        primes.append( 2* i + 1) 
    i = i + 1
    
def isSmith( n) : 
    original_no = n 
    pDigitSum = 0; 
    i=0
    while (primes[i] <= n/2 ) : 
          
        while n % primes[i] == 0 :  
            p = primes[i] 
            n = n/p 
            while p > 0 : 
                pDigitSum += (p % 10) 
                p = p/10
        i=i+1
    if not n == 1 and not n == original_no : 
        while n > 0 : 
            pDigitSum = pDigitSum + n%10
            n=n/10
      
    sumDigits = 0
    while original_no > 0 : 
        sumDigits = sumDigits + original_no % 10
        original_no = original_no/10
           
    return pDigitSum == sumDigits

sieveSundram()
i = 1
while i<500 : 
    if isSmith(i) : 
        print(i)
    i=i+1

