"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    from collections import deque
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node
        
        cloned = {}
        queue=deque()
        queue.append(node)
        cloned[node] = Node(node.val,[])


        while queue:
            cur = queue.popleft()
            for nei in cur.neighbors:
                if nei not in cloned:
                    cloned[nei] = Node(nei.val,[])
                    queue.append(nei)
                cloned[cur].neighbors.append(cloned[nei])
        return cloned[node]