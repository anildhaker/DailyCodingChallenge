# In a string S of lowercase letters, these letters form consecutive groups of the same character.

# For example, a string like S = "abbxxxxzyy" has the groups "a", "bb", "xxxx", "z" and "yy".

# Call a group large if it has 3 or more characters.  We would like the starting and ending positions of every large group.

# The final answer should be in lexicographic order.

 

# Example 1:

# Input: "abbxxxxzzy"
# Output: [[3,6]]
# Explanation: "xxxx" is the single large group with starting  3 and ending positions 6.

class Solution:
    def largeGroupPositions(self, S: str) -> List[List[int]]:
        
        n = len(S)
        left = 0
        right = 0 
        splits = []
        splits_num = []
        result = []
        
        for i in range(1,n):
            if S[i] == S[i-1]:
                right = right + 1
            else:
                splits.append([left,right])
                left = i
                right = i
                
        splits.append([left,right])
            
        for i in range(len(splits)):
            splits_num.append(splits[i][1] - splits[i][0])
                
        for i in range(len(splits)):
            if splits_num[i] >= 2:
                result.append(splits[i])
                    
        return result