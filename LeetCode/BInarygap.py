# Given a positive integer N, find and return the longest distance between two consecutive 1's in the binary representation of N.

# If there aren't two consecutive 1's, return 0.

 

# Example 1:

# Input: 22
# Output: 2
# Explanation: 
# 22 in binary is 0b10110.
# In the binary representation of 22, there are three ones, and two consecutive pairs of 1's.
# The first consecutive pair of 1's have distance 2.
# The second consecutive pair of 1's have distance 1.
# The answer is the largest of these two distances, which is 2.


def binaryGap(self, N):
        index = [i for i, v in enumerate(bin(N)) if v == '1']
        return max([b - a for a, b in zip(index, index[1:])] or [0])