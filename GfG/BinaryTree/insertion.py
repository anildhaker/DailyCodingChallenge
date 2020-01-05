# insertion in level order

class Node:
  def __init__(self, data):
    self.key = data
    self.left = None
    self.right = None

# inOrder Travewrsal

def inOrder(temp):
  if not temp:
    return
  inOrder(temp.left)
  print(temp.key, end=" ")
  inOrder(temp.right)

# insert in binary tree

def insertBT(temp, key):
  q = []

  q.append(temp)

  while (len(q)>0):
    temp = q[0]
    q.pop(0)
    if not temp.left:
      temp.left = Node(key)
      break
    else:
      q.append(temp.left)

    if not temp.right:
      temp.right = Node(key)
      break
    else:
      q.append(temp.right)


root = Node(10)  
root.left = Node(11)  
root.left.left = Node(7)  
root.right = Node(9)  
root.right.left = Node(15)  
root.right.right = Node(8)

print("before adding key -")
inOrder(root)
print()
insertBT(root, 12)
print("After adding key -")
inOrder(root)