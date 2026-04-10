class Solution:
    from collections import deque
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for x in range(numCourses)]
        indegree =[0] * numCourses
        

        for prereq in prerequisites:
            adj[prereq[1]].append(prereq[0])
            indegree[prereq[0]]+=1
        
        queue =[]
        for x in range(numCourses):
            if indegree[x] == 0:
                queue.append(x)
        
        visited = 0
        while queue:
            node = queue.pop(0)
            visited+=1
            for neighbour in adj[node]:
                indegree[neighbour]-=1
                if indegree[neighbour] == 0:
                    queue.append(neighbour)
                    
        return numCourses == visited

        



        

