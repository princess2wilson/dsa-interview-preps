# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()

        queue.append(root)
        ans = []

        while queue:
            arr = []
            for _ in range(len(queue)): 
                node = queue.popleft()
                if not node:
                    continue
                queue.append(node.left)
                queue.append(node.right)
                arr.append(node.val)
            if arr:
                ans.append(arr)
        return ans
