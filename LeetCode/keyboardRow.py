# Given a List of words,
# return the words that can be typed using letters of
# alphabet on only one row's of American keyboard

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        a = set('qwertyuiop')
        b = set('asdfghjkl')
        c = set('zxcvbnm')
        
        ans = []
        for word in words:
            p = set(word.lower())
            
            if a&p == p:
                ans.append(word)
            
            if b&p == p:
                ans.append(word)
            
            if c&p == p:
                ans.append(word)
        
        return ans
            
                
        

