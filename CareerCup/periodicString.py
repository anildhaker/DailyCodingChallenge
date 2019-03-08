# Find whether string S is periodic. 
# Periodic indicates S = nP. 
# e.g. 
# S = "ababab", then n = 3, and P = "ab" 
# S = "xxxxxx", then n = 1, and P = "x" 
# S = "aabbaaabba", then n = 2, and P = "aabba" 

# Given string S, find out the P (repetitive pattern) of S.


def repeat_str(s):
  n = len(s)
  for i in range(1,len(s)):
    if n % i == 0:
      x = s[:i]
      if x * (n // i) == s:
        print(x)
        break
  
repeat_str('abab')
