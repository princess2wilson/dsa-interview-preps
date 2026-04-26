# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        arr =[]
        prev = -float("inf")
        ans = True
        def inorder(root):
            if root is None:
                return 
            inorder(root.left)
            arr.append(root.val)
            inorder(root.right)
        
        inorder(root)
        for x in arr:
            if x<=prev:
                ans = False
                break
            prev = x
        return ans
            

