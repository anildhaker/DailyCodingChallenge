# N-bonacci series -> need to print M terms of n-bonacci series

def bonacciSeries(n,m):
  b = [0] * m
  # keep first n-1 terms zero and nTh = 1
  b[n - 1] = 1
  
  for i in range(n, m):
    for j in range(i - n, i):
      b[i] = b[i] + b[j]

  for i in range(0, m):
    print(b[i], end=" ")
    
  
bonacciSeries(5, 15)
print()