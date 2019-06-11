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


# Second Approach
        # left, right = 0,0
        # longest = 0 
        # p = set()
        # while left < len(s) and right < len(s):
        #     if s[right] not in p:
        #         p.add(s[right])
        #         right += 1 
        #         longest = max(longest,right-left)
        #     else:
        #         p.remove(s[left])
        #         left += 1
                
        # return longest