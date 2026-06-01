# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque()
        queue.append(root)
        res = []

        while queue: 
            right_node = None
            for _ in range(len(queue)):
                node = queue.popleft()
                if node:
                    right_node = node
                    queue.append(node.left)
                    queue.append(node.right)
                    

            if right_node:
                res.append(right_node.val)
        return res


                




        """
        process each level.
        level 1 - 1 we would immediately pop and add
        level 2 - we add the right first. pop and add immediately
        level 3 - no right, we only add left, pop and add immediately
        """