# Question was Asked in Apple Interview
stack1 = []
stack2 = []
class Queue():
  
  def __init__(self):
    pass
  
  def enqueue(self, element):
    stack1.append(element)

  def dequeue(self):
    if len(stack2) == 0:
      if (len(stack1) == 0):
        return
      while (len(stack1) > 0):
        p = stack1.pop()
        stack2.append(p)

    return stack2.pop()


Q = Queue()
Q.enqueue('a')
Q.enqueue('b')
Q.enqueue('c')
print(Q.dequeue())



