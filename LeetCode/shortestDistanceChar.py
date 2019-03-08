# Given a string S and a character C, return an array of integers representing the shortest distance from the character C in the string.

# Example 1:

# Input: S = "loveleetcode", C = 'e'
# Output: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]


class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        
        pos = []  #position of C
        
        for i, v in enumerate(S):
            if v == C :
                pos.append(i)
        
        res = []
        
        for i in range(len(S)):
            res.append(min([abs(t-i) for t in pos]))
            
        return res
        


