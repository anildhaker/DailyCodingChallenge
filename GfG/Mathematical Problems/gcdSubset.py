# Given a set of N elements such that N\in [1, 1000], task is to generate an array
#  such that the GCD of any subset of the generated array lies in the given set of elements.
# The generated array should not be more than thrice the length of the set of the GCD.

# Input : 3
#         1 2 7
# Output :  1 1 2 1 7

# Assume array is sorted 
from math import gcd

def gcdArray(A):
  res = A[0]
  for i in range(len(A)):
    res = gcd(res, A[i])
  return res
  
def computeArr(A):
  x = gcdArray(A)
  ans = []
  if x == A[0]:
    ans.append(A[0])
    for i in range(1,len(A)):
      ans.append(A[0])
      ans.append(A[i])
    
    for i in range(len(ans)):
      print(i,end=" ")

  else:
    print("Array cannot be constructed")

A = [2, 5, 6, 7, 11]
computeArr(A)