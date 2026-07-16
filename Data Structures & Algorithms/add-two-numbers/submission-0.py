# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        curr = dummy
        carry = 0
        suml1l2 = 0

        while l1 or l2:
            suml1l2 = 0
            suml1l2+=carry
            if l1:
                suml1l2+=l1.val
            if l2:
                suml1l2+=l2.val
            
            new = ListNode(suml1l2%10)
            carry = suml1l2//10

            curr.next = new
            curr = curr.next

            if l1:
                l1 = l1.next
            if l2:
                l2=l2.next

        if carry:
            new = ListNode(carry)
            curr.next = new
        return dummy.next