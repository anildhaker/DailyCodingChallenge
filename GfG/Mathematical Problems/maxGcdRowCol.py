# Replace elements of Matrix with max GCD of ROW n Col

R = 3
C = 4

def gcd(a, b):
  if a == 0:
    return b
  return gcd(b % a, a)
  
def replacementMatrix(mat, n, m):
  row_gcd = [0] * n
  col_gcd = [0] * m
  
  for i in range(n):
    for j in range(m):
      row_gcd[i] = gcd(row_gcd[i], mat[i][j])
      col_gcd[j] = gcd(col_gcd[j], mat[i][j])
      
  for i in range(n):
    for j in range(m):
      mat[i][j] = max(row_gcd[i], col_gcd[j])
      
## Driver Code

mat = ([1, 2, 3, 3],
       [4, 5, 6, 6],
       [7, 8, 9, 9])
       
replacementMatrix(mat, R, C)

for i in range(R):
  for j in range(C):
    print(mat[i][j], end=" ")
  print()

  