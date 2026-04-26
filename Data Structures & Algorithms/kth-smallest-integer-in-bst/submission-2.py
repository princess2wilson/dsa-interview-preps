# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.arr =[]
        def dfs(root,arr):
            if root is None:
                return 
            left = dfs(root.left,self.arr)
            
            self.arr.append(root.val)
            right = dfs(root.right,self.arr)

            
         
        dfs(root,self.arr)
        return self.arr[k-1]
        

           
            

            
            
            
       