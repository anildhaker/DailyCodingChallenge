# Input: "abcabcbb"
# Output: 3 
# Explanation: The answer is "abc", with the length of 3. 

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = []
        letters = []
        length_ = 0
        for char in s:
            if char not in letters:
                letters.append(char)
                length_ += 1 
            else:
                l.append(length_)
                length_ = 0 
        return max(l)