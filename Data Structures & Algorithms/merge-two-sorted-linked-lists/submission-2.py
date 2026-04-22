# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        n1 = list1
        n2 = list2

        new_list = ListNode()
        dummy = new_list


        while True:
            if n2==None:
                new_list.next = n1
                break
            if n1==None:
                new_list.next = n2
                break
            if n1.val < n2.val:
                new_list.next = n1
                n1 = n1.next
                new_list = new_list.next
            else:
                new_list.next = n2
                n2 = n2.next
                new_list = new_list.next
        
        return dummy.next
            

            

                
