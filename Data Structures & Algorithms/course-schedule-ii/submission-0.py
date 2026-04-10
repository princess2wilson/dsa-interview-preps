class Solution:
    from collections import defaultdict
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for x in range(numCourses)]
        indegree = [0] *numCourses
        queue = []
        result =[]

        for preq in prerequisites:
            graph[preq[1]].append(preq[0])
            indegree[preq[0]] +=1
        

        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        
        visited = 0
        while queue:
            course = queue.pop(0)
            result.append(course)
            visited+=1
            for x in graph[course]:
                indegree[x]-=1
                if indegree[x] == 0:
                    queue.append(x)
        
        if visited!=numCourses:
            return[]
        return result
