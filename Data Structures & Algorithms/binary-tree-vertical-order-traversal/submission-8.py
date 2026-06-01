# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque,defaultdict
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        hashmap = defaultdict(list)
        queue = deque()
        queue.append((0,root))
        min_col = max_col = 0

        while queue:
            index,node = queue.popleft()
            if node is None:
                continue
            min_col = min(min_col,index)
            max_col = max(max_col,index)
            hashmap[index].append(node.val)
            queue.append((index-1,node.left))
            queue.append((index+1,node.right))
        arr = []
        if not hashmap:
            return []
        for i in range(min_col,max_col+1):
            arr.append(hashmap[i])
        return arr
        

