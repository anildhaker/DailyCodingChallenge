# Given two arrays, write a function to compute their intersection.

# Example 1:

# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2,2]
# Example 2:

# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [4,9]

def intersection_arrays(num1, num2):
  
  res = []
  d = {}
  for num in num1:
    d[num] = d.get(num, 0) + 1
    
  for num in num2:
    if num in d and d[num] > 0:
      res.append(num)
      d[num] -= 1
  return res

