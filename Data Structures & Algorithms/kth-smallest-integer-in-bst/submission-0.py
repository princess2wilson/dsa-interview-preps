# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        n = 0 #to tell us the number of elements we visited
        cur = root #what node we are at currently
        stack = []

        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            n+=1
            if n == k:
                return cur.val
            cur = cur.right

        

            


