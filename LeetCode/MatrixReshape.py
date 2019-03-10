# You're given a matrix represented by a two-dimensional array, and two positive integers r and c representing the row number and column number of the wanted reshaped matrix, respectively.

# The reshaped matrix need to be filled with all the elements of the original matrix in the same row-traversing order as they were.

# If the 'reshape' operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.

# Example 1:
# Input: 
# nums = 
# [[1,2],
#  [3,4]]
# r = 1, c = 4
# Output: 
# [[1,2,3,4]]
# Explanation:
# The row-traversing of nums is [1,2,3,4]. The new reshaped matrix is a 1 * 4 matrix, fill it row by row by using the previous list.


def matrixReshape(self, A, nR, nC):
    if len(A) * len(A[0]) != nR * nC:
        return A
    
    values = [val for row in A for val in row]

    ans = [[None] * nC for _ in range(nR)]
    
    i = 0
    for r in range(nR):
      for c in range(nC):
        ans[r][c] = values[i]
        i += 1

    return ans
      


