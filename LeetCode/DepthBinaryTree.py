# Given a binary tree, find its maximum depth.

# The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

# Note: A leaf is a node with no children.

# Example:

# Given binary tree [3,9,20,null,null,15,7],

#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its depth = 3.

#recursion

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        

#using Stack

    def maxDepth_stack(self, root):
      if not root:
        return
      
      stack = [root]
      h = 0

      while stack:
        next_level = []
        while stack:
          top = stack.pop()
          if top.left:
            next_level.append(top.left)
          if top.right:
            next_level.append(top.right)
        stack = next_level
        h += 1
      return h
