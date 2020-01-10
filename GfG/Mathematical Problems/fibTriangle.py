# print the fibonacci triangle.
# Input : n = 5 
# Output :
# 1 
# 1 2 
# 3 5 8 
# 13 21 34 55 
# 89 144 233 377 610

def fib(f, N) : 
  f[1] = 1
  f[2] = 1
  for i in range(3, N + 1):
    f[i] = f[i - 1] + f[i - 2]

def fibTriangle(n):
  N = int(n * (n + 1) / 2)
  f = [0] * (N + 1)

  fib(f, N)

  count = 0

  for i in range(1, n + 1):
    for j in range(i):
      count = count + 1
      print(f[count]," ", end="")
    print()
fibTriangle(5)
      
            
  
          