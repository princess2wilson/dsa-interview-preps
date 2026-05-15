from collections import defaultdict,deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        inorder = [0] * numCourses
        graph = defaultdict(list)
        queue = deque()
        order = []

        for a,b in prerequisites:
            graph[b].append(a)
            inorder[a]+=1
        
        for inorder_ in range(len(inorder)):
            if inorder[inorder_] ==0:
                queue.append(inorder_)
        
        while queue:
            course = queue.popleft()
            order.append(course)
            for neighbour in graph[course]:
                inorder[neighbour]-=1
                if inorder[neighbour] == 0:
                    queue.append(neighbour)
        if len(order) == numCourses:
            return order
        return []


        




"""
1. you need a graph and indegree list.
2 start off by adding all 0 indegree nodes to a deque queue
3. then pop from queue, check the neighbours, decrement the indegree of each neighbour
4. only add the indegree of 0 neighbours to the queue
"""