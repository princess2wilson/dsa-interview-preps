# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def dfs(root):
            if root is None:
                return [0,0]
            left = dfs(root.left)
            right = dfs(root.right)
            
            withRob = root.val+left[0]+right[0]
            withoutRob = max(left) + max(right)
            self.ans = max(self.ans,withRob,withoutRob)
            return [withoutRob,withRob]
        dfs(root)
        return self.ans