"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        old_to_new = {}
        dummy = head



        while dummy!=None:
            old_to_new[dummy] = Node(0)
            dummy = dummy.next
        
        for old in old_to_new:
            old_to_new[old].val = old.val
            old_to_new[old].next = old_to_new.get(old.next)
            old_to_new[old].random = old_to_new.get(old.random)
        if head is None:
            return None
        return (old_to_new[head])

