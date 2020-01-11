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

def deleteDeepest(root, d_node):
  q = []
  q.append(root)
  while len(q) > 0:
    temp = q.pop(0)
    if temp is d_node:
      temp = None
      return
      
    if temp.right:
      if temp.right is d_node:
        temp.right = None
        return
      else:
        q.append(temp.right)

    if temp.left:
      if temp.left is d_node:
        temp.left = None

      else:
        q.append(temp.left)


def deletion(root, key):
  if root is None:
    return None
  if root.left == None and root.right == None:
    if root.key == key:
      return None
    else:
      return root
      
  key_node = None
  q = []
  q.append(root)
  while (len(q) > 0):
    temp = q.pop(0)
    if temp.data == key:
      key_node = temp
      
    if temp.left:
      q.append(temp.left)
    
    if temp.right:
      q.append(temp.right)

  if key_node:
    x = temp.data
    deleteDeepest(root, temp)
    key_node.data = x

  return root 
  

