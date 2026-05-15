# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = float("-inf")
        def dfs(root):
            if not root:
                return 0 

            leftMax = dfs(root.left)
            rightMax = dfs(root.right)

            if leftMax < 0:
               leftMax = 0
            if rightMax<0:
                rightMax = 0
            self.res = max(self.res,leftMax+rightMax+ root.val)
            return root.val + max(leftMax,rightMax)
        dfs(root)
        return self.res
