# Given an array A of 0s and 1s, we may change up to K values from 0 to 1.

# Return the length of the longest (contiguous) subarray that contains only 1s. 

 

# Example 1:

# Input: A = [1,1,1,0,0,0,1,1,1,1,0], K = 2
# Output: 6
# Explanation: 
# [1,1,1,0,0,1,1,1,1,1,1]
# Bolded numbers were flipped from 0 to 1.  The longest subarray is underlined.


class Solution:
  def longestOnes(self, A: List[int], K: int) -> int:
    sol, s, q = 0, -1, []
    for ix, a in enumerate(A):
      if a == 0:
        q.append(ix)
        if len(q) > K:
          s = q.pop(0)
      sol = max(sol, ix - s)        
    return sol     
