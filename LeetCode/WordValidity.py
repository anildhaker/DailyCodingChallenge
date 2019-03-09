# e are given that the string "abc" is valid.

# From any valid string V, we may split V into two pieces X and Y such that X + Y (X concatenated with Y) is equal to V.  (X or Y may be empty.)  Then, X + "abc" + Y is also valid.

# If for example S = "abc", then examples of valid strings are: "abc", "aabcbc", "abcabc", "abcabcababcc".  Examples of invalid strings are: "abccba", "ab", "cababc", "bac".

# Return true if and only if the given string S is valid.

 

# Example 1:

# Input: "aabcbc"
# Output: true
# Explanation: 
# We start with the valid string "abc".
# Then we can insert another "abc" between "a" and "bc", resulting in "a" + "abc" + "bc" which is "aabcbc".
# Example 2:

# Input: "abcabcababcc"
# Output: true
# Explanation: 
# "abcabcabc" is valid after consecutive insertings of "abc".
# Then we can insert "abc" before the last letter, resulting in "abcabcab" + "abc" + "c" which is "abcabcababcc".


#Brute Force

def is_Valid_Word(S):
  S2 = ''
  while S != S2:
    S, S2 = S.replace('abc', ''), S
    
  return (S == '')
  
# Using Stack 
def is_Valid(S):
  stack = []

  for i in S:
    if i == 'c':
      if stack[-2:] != ['a', 'b']:
        return False
      stack.pop()
      stack.pop()
    else:
      stack.append(i)
  
  return (not stack)

