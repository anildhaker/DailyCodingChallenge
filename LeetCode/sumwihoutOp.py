# Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

# Example 1:

# Input: a = 1, b = 2
# Output: 3


class Solution:
    def getSum(self, a: int, b: int) -> int:
        while b!= 0:
            carry = a&b
            a = a^b
            b = carry<<1
        
        return a
        