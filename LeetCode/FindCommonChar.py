# Given an array A of strings made only from lowercase letters, return a list of all characters that show up in all strings within the list (including duplicates).  For example, if a character occurs 3 times in all strings but not 4 times, you need to include that character three times in the final answer.

# You may return the answer in any order.

 

# Example 1:

# Input: ["bella","label","roller"]
# Output: ["e","l","l"]
# Example 2:

# Input: ["cool","lock","cook"]
# Output: ["c","o"]

from collections import Counter

def commonChar(A):  #A is list of words
  c = Counter(A[0])

  for word in A[1:]:
    d = Counter(word)

    c = c & d
  
  return list(c.elements())
