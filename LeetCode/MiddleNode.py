#finding middle node of a linked list

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        slow = head
        fast = head
        
        while (fast and fast.next):
            slow = slow.next
            fast = fast.next.next
            
        return slow
        