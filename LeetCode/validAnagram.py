# Given two strings s and t , write a function to determine if t is an anagram of s.

# Example 1:

# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:

# Input: s = "rat", t = "car"
# Output: false

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        maps = {}
        mapt = {}
        
        for i in s:
            maps[i] = maps.get(i,0) + 1
            
        for i in t:
            mapt[i] = mapt.get(i,0) + 1
            
        return maps == mapt
            