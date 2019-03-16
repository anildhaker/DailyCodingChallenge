# Given a column title as appear in an Excel sheet, return its corresponding column number.

# For example:

#     A -> 1
#     B -> 2
#     C -> 3
#     ...
#     Z -> 26
#     AA -> 27
#     AB -> 28 
#     ...
# Example 1:

# Input: "A"
# Output: 1
# Example 2:

# Input: "AB"
# Output: 28

class Solution:
    def titleToNumber(self, s: str) -> int:
        s = s[::-1]
        res = 0 
        
        for i,char in enumerate(s):
            res += (ord(char) - 65 + 1 )*(26**i)
        
        return res
        