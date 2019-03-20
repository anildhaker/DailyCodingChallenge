class Node:
  def __init__(self, data):
    self.data = data
    self.next =  None

class Solution:
  def mergeTwoLists2(self, l1, l2):
    if not l1 and not l2:
      return l1 or l2
    if l1.val < l2.val:
        l1.next = self.mergeTwoLists(l1.next, l2)
        return l1

    else:
      l2.next = self.mergeTwoLists(l1, l2.next)
      return l2
        
