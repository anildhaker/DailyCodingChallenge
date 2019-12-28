# Encode any fib number upto - N = 30

n = 30

fib = [0 for i in range(n)]

def largestFibLessorEqual(n):
  fib[0] = 1 #second fib number  
  fib[1] = 2  #third fib number

  i = 2
  while (fib[i - 1] <= n):
    fib[i] = fib[i - 1] + fib[i - 2]
    i += 1
    
  return i - 2
  
def fibEncoding(n):
  index = largestFibLessorEqual(n)

  codeword = ['a' for i in range(index + 2)]
  
  i = index
  
  while (n):
    codeword[i] = '1'
    n = n - fib[i]
    i = i - 1
    
    while (i >= 0 and fib[i] > n):
      codeword[i] = '0'
      i = i - 1
      
  codeword[index + 1] = '1'  # additional digit
  

  return "".join(codeword)


print(fibEncoding(143))
  
