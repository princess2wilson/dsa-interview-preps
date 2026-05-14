from collections import defaultdict,deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        inorder = [0] * numCourses
        graph = defaultdict(list)
        order = []
        queue = deque()


        for a,b in prerequisites:
            inorder[a]+=1
            graph[b].append(a)

        for x in range(numCourses):
            if inorder[x] == 0:
                queue.append(x)

        while queue:
            course = queue.popleft()
            order.append(course)
            for courses in graph[course]:
                inorder[courses]-=1
                if inorder[courses] == 0:
                    queue.append(courses)
        
        if len(order) == numCourses:
            return True
        return False
                        


