# find all divisors of natural number N

def divisors(N):
  i = 1
  while (i <= N):
    if N % i == 0:
      print(i,end=" ")
    i = i + 1
    
# Time complexity = O(N)
# Space = O(1)

# we know that divisors are present in pairs (1,100),(2,50),(4,25)

def divisorsEfficient(N):
  i = 1
  while i * i <= N:
    if N % i == 0:
       
      if N % i == i:
        print(i)
      else:
        print(i, N // i)
    i = i + 1

divisors(100)
print()
divisorsEfficient(100)
  