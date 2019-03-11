# Level Traversal for N-ary tree

# Recursive Approach

class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution(object):
  def __init__(self):
    self.levels = []
    self.length = 0

  def levelTraverse(self, root, level):
    if level == self.length:
      self.levels.append([root.val])
      self.length += 1

    else:
      self.levels[level].append(root.val)

    for child in root.children:
      self.levelTraverse(child, level + 1)

    
  def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if not root:
            return []
        
        self.levelTraverse(root, 0)
        
        return self.levels


# Iterative Approach


class Solution(object):
        
    def levelOrder(self, root):

      if not root:
        return []
      
      res = []
      ln = 0
        # list to associate each node with corresponding level
      lst = [(root, 0)]
      while lst:
          node, level = lst.pop()
          if ln == level:
              res.append([node.val])
              ln += 1
          else:
              res[level].append(node.val)
          lst.extend([ [child, level+1] for child in node.children[::-1] ])
        
      return res
