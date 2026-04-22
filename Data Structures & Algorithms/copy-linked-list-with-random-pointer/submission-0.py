
#Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        old_to_new = {}
        curr = head
            #node = Node(node.val)
            #node.next = curr.next
            #node.random = curr.random
        while curr!=None:
            old_to_new[curr] = Node(curr.val)
            curr = curr.next
        
        for x in old_to_new:
            old_to_new[x].next = old_to_new.get(x.next)
            old_to_new[x].random = old_to_new.get(x.random)

        
        return old_to_new.get(head)
            