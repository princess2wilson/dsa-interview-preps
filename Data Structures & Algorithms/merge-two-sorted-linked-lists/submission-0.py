# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummypt = dummy

        while l1 and l2: #while both arent empty
            if l1.val < l2.val:
                dummypt.next = l1 #the next val is set to whatever l1 head is 
                l1 = l1.next #move the start of l1 to the next val now for next comparisons
            else: #if l2 bigger or if equal take l1 cause if equal we need to pick one and then move the pointer
                dummypt.next = l2
                l2 = l2.next
            dummypt = dummypt.next #move the pointer of our new node regardless every iteration
        
        if l1:
            dummypt.next = l1 #the next should be the remaining of l1
        elif l2:
            dummypt.next = l2
        
        return dummy.next
            
        