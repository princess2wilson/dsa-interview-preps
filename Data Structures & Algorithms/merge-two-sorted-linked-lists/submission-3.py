# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        n1 = list1
        n2 = list2
        dummy = ListNode()
        head = dummy

        while n1 and n2:
            if n1.val < n2.val:
                head.next = n1
                n1 = n1.next
            else:
                head.next = n2
                n2 = n2.next
            head = head.next

        if n1:
            head.next = n1
        else:
            head.next = n2
        return dummy.next






     