# An array is monotonic if it is either monotone increasing or monotone decreasing.

# An array A is monotone increasing if for all i <= j, A[i] <= A[j].  An array A is monotone decreasing if for all i <= j, A[i] >= A[j].

# Return true if and only if the given array A is monotonic.

 

# Example 1:

# Input: [1,2,2,3]
# Output: true
# Example 2:

# Input: [6,5,4,4]
# Output: true

class Solution:
    def isMonotonic(self, A):
       
            x =  all(A[i] <= A[i+1] for i in range(len(A)-1))
        
            y =  all(A[i] >= A[i+1] for i in range(len(A)-1))
        
            if x or y:
                return True
            return False

#Can be returned in one line too.