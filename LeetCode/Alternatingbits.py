# Given a positive integer, check whether it has alternating bits: namely, if two adjacent bits will always have different values.

# Example 1:
# Input: 5
# Output: True
# Explanation:
# The binary representation of 5 is: 101


class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        s1 = set()
        s2 = set()
        
        if n>1:
            for i,j in enumerate(bin(n)[2:]):
                #print(i,j)
                if(i%2==0):
                    s1.add(j)
                else:
                    s2.add(j)

            return(len(s1)==len(s2) and s1!=s2)
        else:
            return True


# One liner Solution

class Solution(object):
    def hasAlternatingBits(self, n):
        bits = bin(n)
        return all(bits[i] != bits[i+1] for i in range(len(bits) - 1))