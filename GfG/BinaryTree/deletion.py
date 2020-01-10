# delete a given node in binary tree and replace it with the bottom-right node

class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None
    
# inOrder traversal
def inOrder(temp):
  if temp is None:
    return
    
  inOrder(temp.left)
  print(temp.data, end=" ")
  inOrder(temp.right)