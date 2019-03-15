# Given a binary array, find the maximum number of consecutive 1s in this array.

# Example 1:
# Input: [1,1,0,1,1,1]
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive 1s.
#     The maximum number of consecutive 1s is 3.

class Solution:
    def findMaxConsecutiveOnes(self, nums):
        n = 0
        maxn = 0
        for i,v in enumerate(nums):
            if v == 1:
                n += 1
            else:
                maxn = max(maxn, n)
                n = 0
        maxn = max(maxn, n)
        return maxn