# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = -float("inf")

        def dfs(root):
            if root is None:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)

            if left < 0:
                left = 0
            if right < 0:
                right = 0
            self.res = max(self.res,root.val+left+right)
            return root.val + max(left,right)
        dfs(root)
        return self.res


