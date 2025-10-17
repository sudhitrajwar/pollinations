# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0, head)
        slow = fast = dummy
        
        # Move fast n+1 steps ahead to keep a gap of n between fast and slow
        for _ in range(n + 1):
            fast = fast.next
        
        # Move both until fast reaches the end
        while fast:
            slow = slow.next
            fast = fast.next
        
        # Delete the nth node from end
        slow.next = slow.next.next
        
        return dummy.next
