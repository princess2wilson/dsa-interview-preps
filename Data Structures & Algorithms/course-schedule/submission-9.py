from collections import defaultdict,deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        queue = deque()
        graph = defaultdict(list)
        inorder = [0] * numCourses
        courses = []

        for a,b in prerequisites:
            graph[b].append(a)
            inorder[a]+=1
        for x in range(numCourses):
            if inorder[x] == 0:
                queue.append(x)

        while queue:
            node = queue.popleft()
            courses.append(node)
            for nei in graph[node]:
                inorder[nei]-=1
                if inorder[nei] == 0:
                    queue.append(nei)
        if len(courses) == numCourses:
            return True
        return False

        
