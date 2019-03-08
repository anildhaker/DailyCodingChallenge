# Consider all the leaves of a binary tree.
# From left to right order, the values of those leaves form a leaf value sequence.


# For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

# Two binary trees are considered leaf-similar if their leaf value sequence is the same.

# Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        return self.findleaf(root1) == self.findleaf(root2)

    def findleaf(self,root):
        if not root:
            return []
        
        if (root.left == None and root.right == None):
            return [root.val]
        
        return self.findleaf(root.left) + self.findleaf(root.right)