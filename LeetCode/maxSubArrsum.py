# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

# Example:

# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.


def max_subArrSum(A):
  for i in range(len(A)):
    if A[i] > 0:
      A[i + 1] += A[i]
  return max(A)

# Brilliant Approach 