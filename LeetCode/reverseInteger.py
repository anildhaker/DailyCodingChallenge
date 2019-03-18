# Given a 32-bit signed integer, reverse digits of an integer.

# Example 1:

# Input: 123
# Output: 321
# Example 2:

# Input: -123
# Output: -321

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        s=0
        y=abs(x)
        while (y!=0):
        
            t = y % 10
            s = s * 10 + t
            y = y // 10
        
        lim=2 ** 31-1
    
        if abs(x) > lim: 
            return 0
        if abs(s) > lim: 
            return 0
        if x!=0: 
            return int(x/abs(x)*s)
        return 0