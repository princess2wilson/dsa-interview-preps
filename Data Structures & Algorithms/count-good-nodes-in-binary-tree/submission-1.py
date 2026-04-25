# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        curr = root
        self.counter = 0
        largest = -float("inf")
        def dfs(curr,largest):
            if curr is None:
                return
            if curr.val>=largest:
                largest = max(largest,curr.val) 
                self.counter+=1
            dfs(curr.right,largest)
            dfs(curr.left,largest)
        
           

        dfs(root,largest)
        return self.counter
                


