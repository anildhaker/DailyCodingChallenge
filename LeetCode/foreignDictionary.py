# n an alien language, surprisingly they also use english lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

# Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographicaly in this alien language.

 

# Example 1:

# Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
# Output: true
# Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.


class Solution:
    def isAlienSorted(self, words, order):
        lookup = {ch: i for i, ch in enumerate(order)}
        X = sorted(words, key=lambda word: [lookup[ch] for ch in word])
        return X == words