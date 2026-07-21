# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        prev = dummy

        for _ in range(left-1):
            prev = prev.next
        curr = prev.next
        
        for _ in range(right-left):
            node = curr.next
            curr.next = curr.next.next
            node.next = prev.next
            prev.next = node
        return dummy.next
            
            
            



    
        
        
        
