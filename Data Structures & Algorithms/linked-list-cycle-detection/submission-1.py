# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()
        curr = head

        while curr is not None:
            if (curr.val,curr.next) not in seen:
                seen.add((curr.val,curr.next))
                curr = curr.next
            else:
                return True
        return False
           
        

        
