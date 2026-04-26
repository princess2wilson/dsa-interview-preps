# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = -float("inf")
        def dfs(root):
            
            if not root:
                return 0
            leftmax =dfs(root.left)
            rightmax = dfs(root.right)

            if leftmax < 0:
                leftmax =0
            if rightmax <0:
                rightmax =0

            self.max_sum = max(self.max_sum,leftmax+rightmax+root.val)
            return root.val+max(leftmax,rightmax)
        dfs(root)
        return self.max_sum
