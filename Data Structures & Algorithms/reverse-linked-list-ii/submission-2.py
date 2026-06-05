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
            curr.next = node.next
            node.next = prev.next
            prev.next = node
        return dummy.next

        """
        Say you have `1 → 2 → 3 → 4 → 5` and want to reverse positions 2–4.

- `prev` sits at node 1 (just before the section)
- `curr` sits at node 2 (start of the section — it never moves)
- Each loop: grab the node in front of `curr` and slot it right after `prev`
        """
            
