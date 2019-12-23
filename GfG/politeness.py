# Find politeness of a number
# Given an integer n. Find politeness of number n. Politeness of a number is
# defined as the number of ways it can be expressed as the sum of consecutive integers.

# Input: n = 15
# Output: 3
# Explanation:
# There are only three ways to express
# 15 as sum of consecutive integers i.e.,
# 15 = 1 + 2 + 3 + 4 + 5
# 15 = 4 + 5 + 6
# 15 = 7 + 8
# Hence answer is 3

# Input: n = 9;
# Output:  2
# There are two ways of representation:
# 9 = 2 + 3 + 4
# 9 = 4 + 5

# The idea is to represent N as a sequence of length L+1 as:
# N = a + (a+1) + (a+2) + .. + (a+L)
# => N = (L+1)*a + (L*(L+1))/2
# => a = (N- L*(L+1)/2)/(L+1)
# We substitute the values of L starting from 1 till L*(L+1)/2 < N
# If we get 'a' as a natural number then the solution should be counted.

def politeness(N):
  count = 0
  L = 1
  while (L * (L + 1) < 2 * N):
    a = (1.0 * N - (L * (L + 1)) / 2) / (L + 1)
    if (a - int(a) == 0.0): # cheking if a is natural number 
      count += 1
    L += 1
  return count

print(politeness(10))
print(politeness(15))

    
 
  
    
      
  
  