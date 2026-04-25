# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        count = 0 
    

        def dfs(root):
            if root == None:
                return [0,0]
            leftMax = dfs(root.left)
            rightMax = dfs(root.right)

            maxwithNode = root.val+leftMax[1] + rightMax[1]
            maxwithoutNode = max(leftMax) + max(rightMax)
            
            return [maxwithNode,maxwithoutNode]
        
        return max(dfs(root))

            

